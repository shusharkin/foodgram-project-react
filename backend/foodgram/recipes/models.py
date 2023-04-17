from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models

User = get_user_model()


class Ingredient(models.Model):
    """Описывает модель ингредиентов"""

    name = models.CharField(max_length=100, verbose_name='Название')

    measure = models.CharField(
        max_length=200,
        verbose_name='Единица измерения'
    )

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return self.name


class Tag(models.Model):
    """Описывает модель тегов"""

    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Название'
    )

    color = models.CharField(max_length=7, unique=True, verbose_name='Цвет')

    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """Описывает модель рецептов"""

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор рецепта'
    )

    name = models.CharField(max_length=100, verbose_name='Название')

    image = models.FileField(
        upload_to='recipe_image/',
        verbose_name='Изображение'
    )

    text = models.TextField()

    ingredients = models.ManyToManyField(
        Ingredient,
        related_name='recipes',
        verbose_name='Ингредиенты'
    )

    tags = models.ManyToManyField(
        Tag,
        related_name='tags',
        verbose_name='Теги'
    )

    cooking_time = models.PositiveIntegerField(
        verbose_name='Время приготовления, мин',
        validators=(validators.MinValueValidator(
            1, message='Минимальное время приготовления 1 минута'),
        )
    )

    class Meta:
        # Сортировка по дате публикации
        ordering = ('-id',)
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    """Модель для связи рецептов и ингредиентов"""

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='amount',
        verbose_name='Рецепт'
    )

    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='recipe_ingredients',
        verbose_name='Ингредиенты рецепта'
    )

    amount = models.PositiveIntegerField(
        verbose_name='Количество',
        validators=(validators.MinValueValidator(
            1, message='Нужно добавить хотя бы один ингредиент'),
        )
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Количество ингредиента'
        verbose_name_plural = 'Количество ингредиентов'
        # В рецепте ингредиент можно использовать только один раз
        constraints = [
            models.UniqueConstraint(
                fields=['recipe', 'ingredient'],
                name='unique_recipe_ingredient'
            )
        ]
        db_table = 'recipes_recipe_ingredient'

    def __str__(self):
        return self.ingredient.name


class Favorite(models.Model):
    """Описывает модель избранного"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='Хозяин избранного'
    )

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='Рецепт из избранного'
    )

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'
        # Добавить рецепт можно только один раз
        constraints = [
            models.UniqueConstraint(
                fields=('user', 'recipe'),
                name='unique_favorite_recipes'
            )
        ]

    def __str__(self):
        return f'Рецепт {self.recipe_id} добавлен в избранное пользователю {self.user_id}'


class ShoppingList(models.Model):
    """Описывает модель списка покупок"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='shopping_list',
        verbose_name='Хозяин списка покупок'
    )

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='shopping_list',
        verbose_name='Список покупок'
    )

    class Meta:
        verbose_name = 'Список покупок'
        verbose_name_plural = 'Списки покупок'
        # Добавить рецепт можно только один раз
        constraints = [
            models.UniqueConstraint(
                fields=('user', 'recipe'),
                name='unique_cart_user_recipes'
            )
        ]

    def __str__(self):
        return f'Рецепт {self.recipe_id} добавлен в список покупок пользователю {self.user_id}'
