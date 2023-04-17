from django.contrib import admin

from .models import (Favorite, Ingredient, Recipe, RecipeIngredient,
                     ShoppingList, Tag)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    # Настройка отображения ингредиентов

    list_display = (
        'name',
        'measure',
    )

    search_fields = (
        'name',
    )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    # Настройка отображения тегов

    list_display = (
        'name',
        'color',
        'slug'
    )

    search_fields = (
        'name',
    )


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    # Настройка отображения рецептов

    list_display = (
        'author',
        'name',
        'image',
        'view_text',
        'cooking_time',
        'favorite_cnt',
    )

    search_fields = (
        'name',
        'author',
        'tags'
    )

    readonly_fields = ('favorite_cnt',)

    @staticmethod
    def view_text(obj):
        return obj.text[:100]

    @staticmethod
    def favorite_cnt(obj):
        return obj.favorites.select_related('user').count()


@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
    # Настройка отображения ингредиентов рецепта

    list_display = (
        'recipe',
        'ingredient',
        'amount',
    )

    search_fields = (
        'ingredient',
    )


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    # Настройка отображения избранного
    list_display = (
        'user',
        'recipe',
    )
    search_fields = (
        'user',
    )


@admin.register(ShoppingList)
class ShoppingListAdmin(admin.ModelAdmin):
    # Настройка отображения списка покупок

    list_display = (
        'user',
        'recipe',
    )

    search_fields = (
        'user',
    )
