from django.contrib.auth import get_user_model
from django.db import models

from core.models import TimestampedModel
from core.utils import cut_string

User = get_user_model()


class Topic(models.Model):
    '''Сущность `Темы`.'''

    title = models.CharField(
        'название',
        max_length=200,
        unique=True,
        help_text='Введите название темы',
    )

    class Meta:
        verbose_name = 'тема'
        verbose_name_plural = 'темы'

    def __str__(self) -> str:
        return cut_string(self.title)


class Post(TimestampedModel):
    '''Сущность `Посты`.'''

    topic = models.ManyToManyField(
        Topic,
        verbose_name='темы поста',
        help_text='Введите темы поста',
    )
    content = models.TextField(
        'содержимое поста',
        help_text='Введите содержимое поста',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='автор',
        help_text='Введите автора поста',
    )

    class Meta(TimestampedModel.Meta):
        verbose_name = 'пост'
        verbose_name_plural = 'посты'

    def __str__(self) -> str:
        return cut_string(self.content)


class Like(models.Model):
    '''Сущность `Лайки`.'''

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='пользователь',
        help_text='Выберите пользователя, который ставит лайк',
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='пост',
        help_text='Выберите пост',
    )

    class Meta:
        verbose_name = 'лайк'
        verbose_name_plural = 'лайки'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'post'],
                name='unique_likes',
            ),
        ]

    def __str__(self) -> str:
        return f'`{self.user}` поставил лайк `{self.post}`'
