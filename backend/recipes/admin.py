from django.contrib import admin

from recipes.models import (
    Favorite,
    IngredientsModel,
    RecipeIngredient,
    RecipesModel,
    ShoppingCart,
    TagsModel
)


@admin.register(IngredientsModel)
class IngredientsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'measurement_unit',
    )
    search_fields = (
        'name',
    )


@admin.register(TagsModel)
class TagsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'color',
        'slug'
    )
    search_fields = (
        'name',
    )


@admin.register(RecipesModel)
class RecipesAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'name',
        'image',
        'view_text',
        'cooking_time',
        'count_favorite',
    )
    search_fields = (
        'name',
        'author',
        'tags'
    )

    readonly_fields = ('count_favorite',)

    @staticmethod
    def view_text(obj):
        return obj.text[:100]

    @staticmethod
    def count_favorite(obj):
        return obj.favorites.select_related('user').count()


@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
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
    list_display = (
        'user',
        'recipe',
    )
    search_fields = (
        'user',
    )


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'recipe',
    )
    search_fields = (
        'user',
    )
