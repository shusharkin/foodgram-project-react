from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class UserFoodgram(AbstractUser):
    """Описывает кастомную модель пользователя"""

    username = models.CharField(
        'username',
        max_length=150,
        unique=True,
        help_text='Не более 150 символов. Только буквы, цифры и @/./+/-/_.',
        error_messages={
            'unique': "Пользователь с таким именем уже существует.",
        },
    )

    password = models.CharField(
        'password',
        max_length=150,
    )

    email = models.EmailField(
        'email address',
        blank=False,
        unique=True,
    )

    first_name = models.CharField(
        'first name',
        max_length=150,
        blank=False,
    )

    last_name = models.CharField(
        'last name',
        max_length=150,
        blank=False,
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Follow(models.Model):
    """Описывает модель подписок на пользователей"""

    user = models.ForeignKey(
        UserFoodgram,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик'
    )
    author = models.ForeignKey(
        UserFoodgram,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор'
    )

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'
        # Запрет подписки самого на себя
        constraints = [
            models.UniqueConstraint(
                fields=('user', 'author'),
                name='unique_followers'
            )
        ]

    def __str__(self):
        return f'{self.user_id} подписан на {self.author_id}'
