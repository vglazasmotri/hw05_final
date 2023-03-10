import shutil
import tempfile
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.cache import cache
from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase, Client, override_settings
from django.urls import reverse
from django import forms
from ..models import Group, Post, Follow
from ..paginators import OBJECTS_PER_PAGE

TEMP_MEDIA_ROOT = tempfile.mkdtemp(dir=settings.BASE_DIR)
User = get_user_model()
TEST_OF_POST: int = 13
ADDED_COMMENTS: int = 1


class PaginatorViewsTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth')
        cls.group = Group.objects.create(
            title='Тестовая группа',
            slug='test_group',
        )
        gen_posts_list: list = []
        for i in range(TEST_OF_POST):
            gen_posts_list.append(
                Post(
                    text=f'Тестовый текст {i}',
                    group=cls.group,
                    author=cls.user,
                )
        )
        Post.objects.bulk_create(gen_posts_list)
        cls.pages = [
            reverse('posts:main'),
            reverse('posts:group', kwargs={'slug': f'{cls.group.slug}'}),
            reverse(
                'posts:profile', kwargs={'username': f'{cls.user.username}'}
            ),
        ]

    def setUp(self):
        cache.clear()
        self.guest_client = Client()
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_correct_page_context_guest_client(self):
        '''Количество постов на 1й и 2й страницах для гостя.'''
        for page in self.pages:
            response1 = self.guest_client.get(page)
            response2 = self.guest_client.get(page + '?page=2')
            count_posts1 = len(response1.context['page_obj'])
            count_posts2 = len(response2.context['page_obj'])
            self.assertEqual(count_posts1, OBJECTS_PER_PAGE)
            self.assertEqual(count_posts2, TEST_OF_POST - OBJECTS_PER_PAGE)

    def test_correct_page_context_authorized_client(self):
        '''Количество постов на 1й и 2й страницах
        для авторизированного пользователя.'''
        for page in self.pages:
            response1 = self.authorized_client.get(page)
            response2 = self.authorized_client.get(page + '?page=2')
            count_posts1 = len(response1.context['page_obj'])
            count_posts2 = len(response2.context['page_obj'])
            self.assertEqual(count_posts1, OBJECTS_PER_PAGE)
            self.assertEqual(count_posts2, TEST_OF_POST - OBJECTS_PER_PAGE)


@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class ViewsTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth')
        cls.user2 = User.objects.create_user(username='auth2')
        cls.group = Group.objects.create(
            title='Тестовая группа',
            slug='test_group',
        )
        small_gif = (            
             b'\x47\x49\x46\x38\x39\x61\x02\x00'
             b'\x01\x00\x80\x00\x00\x00\x00\x00'
             b'\xFF\xFF\xFF\x21\xF9\x04\x00\x00'
             b'\x00\x00\x00\x2C\x00\x00\x00\x00'
             b'\x02\x00\x01\x00\x00\x02\x02\x0C'
             b'\x0A\x00\x3B'
        )
        cls.uploaded = SimpleUploadedFile(
            name='small.gif',
            content=small_gif,
            content_type='image/gif'
        )
        cls.post = Post.objects.create(
            text='Тестовый текст',
            group=cls.group,
            author=cls.user,
            image=cls.uploaded,
        )

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        shutil.rmtree(TEMP_MEDIA_ROOT, ignore_errors=True)

    def setUp(self):
        cache.clear()
        self.guest_client = Client()
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_post_detail_page_show_correct_context(self):
        """Проверка контекста шаблона post_detail."""
        response = self.authorized_client.get(
            reverse('posts:post_detail', kwargs={'post_id': self.post.id})
        )
        post_context = {
            response.context['post'].text: self.post.text,
            response.context['post'].group: self.group,
            response.context['post'].author: self.user.username,
            response.context['post'].image: self.uploaded,
        }
        for value, expected_value in post_context.items():
            self.assertEqual(post_context[value], expected_value)

    def test_post_create_page_show_correct_context(self):
        """Проверка контекста шаблона post_create."""
        response = self.authorized_client.get(reverse('posts:post_create'))
        form_fields = {
            'text': forms.fields.CharField,
            'group': forms.fields.ChoiceField,
        }
        for value, expected_value in form_fields.items():
            with self.subTest(value=value):
                form_field = response.context.get('form').fields.get(value)
                self.assertIsInstance(form_field, expected_value)

    def test_post_create_redirect(self):
        """Редирект после создания поста."""
        form_data = {'text': 'Тестовый текст', 'group': self.group.id}
        response = self.authorized_client.post(
            reverse('posts:post_create'),
            data=form_data,
            follow=True,
        )
        self.assertRedirects(response, reverse(
                'posts:profile', kwargs={'username': f'{self.user.username}'}
            )
        )

    def test_post_edit_page_show_correct_context(self):
        """Проверка контекста шаблона post_edit."""
        response = self.authorized_client.get(
            reverse('posts:post_edit', kwargs={'post_id': self.post.id}))
        form_fields = {
            'text': forms.fields.CharField,
            'group': forms.fields.ChoiceField}
        for value, expected_value in form_fields.items():
            with self.subTest(value=value):
                form_field = response.context.get('form').fields.get(value)
                self.assertIsInstance(form_field, expected_value)

    def test_post_edit_redirect(self):
        '''Валидная форма редактирует пост.'''
        new_group = Group.objects.create(title='Тестовая группа2',
                                         slug='test-group',
                                         description='Описание')
        form_data = {'text': 'Текст записанный в форму',
                     'group': new_group.id}
        response = self.authorized_client.post(
            reverse('posts:post_edit', kwargs={'post_id': self.post.id}),
            data=form_data,
            follow=True)
        self.assertRedirects(response, reverse(
            'posts:post_detail',
            kwargs={'post_id': self.post.id}))

    def test_post_added_correct(self):
        """Пост при создании добавлен корректно"""
        post = Post.objects.create(
            text='Тестовый текст проверка как добавился',
            author=self.user,
            group=self.group,
            image=self.uploaded,
        )
        response_index = self.authorized_client.get(
            reverse('posts:main'))
        response_group = self.authorized_client.get(
            reverse('posts:group',
                    kwargs={'slug': f'{self.group.slug}'}))
        response_profile = self.authorized_client.get(
            reverse('posts:profile',
                    kwargs={'username': f'{self.user.username}'}))
        index = response_index.context['page_obj']
        group = response_group.context['page_obj']
        profile = response_profile.context['page_obj']
        self.assertIn(post, index, 'поста нет на главной странице сайта')
        self.assertIn(post, group, 'поста нет на странице выбранной группы')
        self.assertIn(post, profile, 'поста нет в профайле пользователя')

    def test_post_added_correctly_user2(self):
        """Пост при создании не добавляется другому пользователю
        Но виден на главной и в группе."""
        group2 = Group.objects.create(
            title='Тестовая группа 2',
            slug='test_group2')
        posts_count = Post.objects.filter(group=self.group).count()
        post = Post.objects.create(
            text='Тестовый пост от другого автора',
            author=self.user2,
            group=group2)
        response_profile = self.authorized_client.get(
            reverse('posts:profile',
                    kwargs={'username': f'{self.user.username}'}))
        group = Post.objects.filter(group=self.group).count()
        profile = response_profile.context['page_obj']
        self.assertEqual(group, posts_count, 'Поста нет в другой группе.')
        self.assertNotIn(post, profile, 'Пост в профиле другого пользователя.')

    def test_views_correct_template(self):
        '''Проверка namespace:name использует правильный шаблон.'''
        url_names_templates = {
            reverse(
                'posts:main'
            ): 'posts/index.html',
            reverse(
                'posts:group', kwargs={'slug': f'{self.group.slug}'}
            ): 'posts/group_list.html',
            reverse(
                'posts:profile', kwargs={'username': f'{self.user.username}'}
            ): 'posts/profile.html',
            reverse(
                'posts:post_detail', kwargs={'post_id': self.post.id}
            ): 'posts/post_detail.html',
            reverse(
                'posts:post_create'
            ): 'posts/create_post.html',
            reverse(
                'posts:post_edit', kwargs={'post_id': self.post.id}
            ): 'posts/create_post.html',
            }
        for adress, template in url_names_templates.items():
            with self.subTest(adress=adress):
                response = self.authorized_client.get(adress)
                self.assertTemplateUsed(response, template)

    def test_comment_create_authorized_client(self):
        """Появление коментария после отправки
        авторизированным пользователем и гостем."""
        start_coments_count = self.post.comments.count()
        form_data = {'text': 'Текст тестового комментария'}
        response_guest = self.guest_client.post(
            reverse('posts:add_comment', kwargs={'post_id': self.post.id}),
            data=form_data,
            follow=True,
        )
        response_user = self.authorized_client.post(
            reverse('posts:add_comment', kwargs={'post_id': self.post.id}),
            data=form_data,
            follow=True,
        )
        self.assertRedirects(
            response_guest,
            f'/auth/login/?next=/posts/{self.post.id}/comment/',
        )
        self.assertEqual(
            response_user.context['comments'].count(),
            start_coments_count + ADDED_COMMENTS,
        )

    def test_cache_index(self):
        """Проверка кеша для главной страницы."""
        post_for_del = Post.objects.create(
            text='Тест кеша',
            group=self.group,
            author=self.user,
            image=self.uploaded,
        )
        response_index = self.authorized_client.get(reverse('posts:main'))
        before_del = response_index.content

        post_for_del.delete()
        response_index = self.authorized_client.get(reverse('posts:main'))
        after_del = response_index.content
        self.assertEqual(before_del, after_del)

        cache.clear()
        response_index = self.authorized_client.get(reverse('posts:main'))
        after_clear = response_index.content
        self.assertNotEqual(before_del, after_clear)


class FollowViewsTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth1')
        cls.user2 = User.objects.create_user(username='auth2')
        cls.author = User.objects.create_user(username='someauthor')

    def setUp(self):
        self.guest_client = Client()
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)
        self.authorized_client2 = Client()
        self.authorized_client2.force_login(self.user2)

    def test_following(self):
        """Проверка авторизованный пользователь может подписываться на других
        пользователей и удалять их из подписок."""
        folow_start_count = Follow.objects.filter(user=self.user).count()
        self.authorized_client.post(
            reverse('posts:profile_follow',
                    kwargs={'username': self.author.username}),
        )
        folow_after_add_count = Follow.objects.filter(user=self.user).count()
        self.assertNotEqual(folow_start_count, folow_after_add_count)

        self.authorized_client.post(
            reverse('posts:profile_unfollow',
                    kwargs={'username': self.author.username}),
        )
        folow_after_dell_count = Follow.objects.filter(user=self.user).count()
        self.assertEqual(folow_start_count, folow_after_dell_count)

    def test_follower_and_unfollower_see_new_post(self):
        '''Новая запись пользователя появляется в ленте тех, кто на него
        подписан и не появляется в ленте тех, кто не подписан.'''
        new_post_follower = Post.objects.create(
            author=self.author,
            text='Текстовый текст')
        Follow.objects.create(user=self.user,
                              author=self.author)
        response_follower = self.authorized_client.get(
            reverse('posts:follow_index'))
        new_posts = response_follower.context['page_obj']
        self.assertIn(new_post_follower, new_posts)
        response_unfollower = self.authorized_client2.get(
            reverse('posts:follow_index'))
        new_post_unfollower = response_unfollower.context['page_obj']
        self.assertNotIn(new_post_follower, new_post_unfollower)
