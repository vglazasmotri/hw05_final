from django.contrib.auth import get_user_model
from django.test import TestCase
from ..models import Group, Post, CHAR_MAX

User = get_user_model()


class PostModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth')
        cls.group = Group.objects.create(
            title='Тестовая группа',
            slug='Тестовый слаг',
            description='Тестовое описание',
        )
        cls.post = Post.objects.create(
            author=cls.user,
            text='Тестовый пост',
        )

    def test_post_model_have_correct_object_names(self):
        """Проверяем, что у модели post корректно работает __str__."""
        self.assertEqual(str(self.post),
                         self.post.text[:CHAR_MAX])

    def test_group_model_have_correct_object_names(self):
        """Проверяем, что у модели group корректно работает __str__."""
        self.assertEqual(str(self.group),
                         self.group.title)

    def test_title_help_text(self):
        """Проверка заполнения help_text"""
        field_help_texts = {'text': 'Текст нового поста',
                            'group': 'Группа, к которой будет относиться пост'}
        for field, expected_value in field_help_texts.items():
            with self.subTest(field=field):
                error_name = f'Поле {field} ожидало значение {expected_value}'
                self.assertEqual(
                    self.post._meta.get_field(field).help_text,
                    expected_value, error_name)

    def test_title_label(self):
        """Проверка заполнения verbose_name"""
        field_verboses = {'text': 'Текст поста',
                          'pub_date': 'Дата публикации',
                          'group': 'Группа',
                          'author': 'Автор'}
        for field, expected_value in field_verboses.items():
            with self.subTest(field=field):
                error_name = f'Поле {field} ожидало значение {expected_value}'
                self.assertEqual(
                    self.post._meta.get_field(field).verbose_name,
                    expected_value, error_name)
