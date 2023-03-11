from django.db import models
from django.contrib.auth import get_user_model
from .validators import validate_not_empty

User = get_user_model()
CHAR_MAX = 15


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(
        verbose_name='Текст поста',
        help_text='Текст нового поста',
        validators=[validate_not_empty],
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
    )
    group = models.ForeignKey(
        Group,
        blank=True, null=True,
        on_delete=models.SET_NULL,
        verbose_name='Группа',
        help_text='Группа, к которой будет относиться пост',
    )
    image = models.ImageField(
        'Картинка',
        upload_to='posts/',
        blank=True
    )

    class Meta:
        default_related_name = 'posts'
        ordering = ['-pub_date']

    def __str__(self):
        return self.text[:CHAR_MAX]


class Comment(models.Model):
    text = models.TextField(
        verbose_name='Текст комментария',
        help_text='Напишите комментарий',
    )
    created = models.DateTimeField(
        verbose_name='Дата и время публикации',
        auto_now_add=True,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='Пост',
    )

    class Meta:
        default_related_name = 'comments'
        ordering = ['-created']

    def __str__(self):
        return self.text[:CHAR_MAX]


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following'
    )

    class Meta:
        ordering = ['-author']
        verbose_name = 'Подписки на авторов'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'author'], name='unique_follow'
            ),
            models.CheckConstraint(
                check=~models.Q(author=models.F('user')),
                name='can_not_follow_yourself'
            ),
        ]