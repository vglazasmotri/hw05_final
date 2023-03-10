from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.test import TestCase, Client
from http import HTTPStatus
from ..models import Group, Post

User = get_user_model()


class CorrectURLTests(TestCase):
    def setUp(self):
        cache.clear()
        self.guest_client = Client()
        self.user = User.objects.create_user(username='NameUser1')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)
        self.post = Post.objects.create(text='Тестовый текст',
                                        author=self.user)
        self.group = Group.objects.create(title='Тестовая группа',
                                          slug='test_group')
        self.main_url = '/'
        self.group_url = f'/group/{self.group.slug}/'
        self.profile_url = f'/profile/{self.user.username}/'
        self.post_detail_url = f'/posts/{self.post.id}/'
        self.post_create_url = '/create/'
        self.post_edit_url = f'/posts/{self.post.id}/edit/'
        self.guest_redirect_post_create_url = '/auth/login/?next=/create/'
        self.guest_redirect_post_edit_url = self.post_detail_url
        self.unexisting_page_url = '/unexisting_page/'

    def test_urls_uses_correct_template(self):
        """URL-адрес использует соответствующий шаблон."""
        templates_url_names = {
            self.main_url: 'posts/index.html',
            self.group_url: 'posts/group_list.html',
            self.profile_url: 'posts/profile.html',
            self.post_detail_url: 'posts/post_detail.html',
            self.post_create_url: 'posts/create_post.html',
            self.post_edit_url: 'posts/create_post.html',
        }
        for address, template in templates_url_names.items():
            with self.subTest(address=address):
                response = self.authorized_client.get(address)
                error_name = f'Ошибка: {address} ожидал шаблон {template}'
                self.assertTemplateUsed(response, template, error_name)

    def test_urls_guest_client(self):
        """Доступ неавторизованного пользователя"""
        pages: tuple = (self.main_url,
                        self.group_url,
                        self.profile_url,
                        self.post_detail_url)
        for page in pages:
            response = self.guest_client.get(page)
            error_name = f'Ошибка: нет доступа к странице {page}'
            self.assertEqual(
                response.status_code,
                HTTPStatus.OK, error_name)

    def test_urls_redirect_guest_client(self):
        """Редирект неавторизованного пользователя"""
        pages = {
            self.post_create_url: self.guest_redirect_post_create_url,
            self.post_edit_url: self.guest_redirect_post_edit_url}
        for page, value in pages.items():
            response = self.guest_client.get(page)
            self.assertRedirects(response, value)

    def test_urls_authorized_client(self):
        """Доступ авторизованного пользователя"""
        pages = (
            self.post_create_url,
            self.post_edit_url,
        )
        for page in pages:
            response = self.authorized_client.get(page)
            error_name = f'Ошибка: нет доступа к странице {page}'
            self.assertEqual(response.status_code, HTTPStatus.OK, error_name)

    def test_unexisting_page(self):
        """Код несуществующей страницы 404"""
        response = self.guest_client.get(self.unexisting_page_url)
        self.assertEqual(response.status_code, 404)
