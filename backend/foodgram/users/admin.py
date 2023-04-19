from django.contrib import admin
from django.contrib.auth import get_user_model

from users.models import Follow

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # Настройка отображения пользователей
    list_display = (
        'id',
        'username',
        'first_name',
        'last_name',
        'email',
    )
    search_fields = (
        'email',
        'username',
        'first_name',
    )


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    # Настройка отображения подписок
    list_display = (
        'user',
        'author'
    )
    search_fields = (
        'user',
    )
