from django.shortcuts import get_object_or_404
from recipes.models import RecipesModel
from rest_framework import status
from rest_framework.response import Response


def delete_obj(request, pk, model):
    recipe = get_object_or_404(RecipesModel, pk=pk)
    if model.objects.filter(user=request.user, recipe=recipe).exists():
        follow = get_object_or_404(
            model,
            user=request.user,
            recipe=recipe
        )
        follow.delete()
        return Response(
            'Рецепт удален',
            status=status.HTTP_204_NO_CONTENT
        )
    return Response(
        {'errors': 'Нельзя удалить рецепт, который не был добавлен'},
        status=status.HTTP_400_BAD_REQUEST
    )


def post_obj(request, pk, model, serializer):
    recipe = get_object_or_404(RecipesModel, pk=pk)
    if model.objects.filter(user=request.user, recipe=recipe).exists():
        return Response(
            {'errors': 'Рецепт уже был добавлен'},
            status=status.HTTP_400_BAD_REQUEST,
        )
    model.objects.get_or_create(user=request.user, recipe=recipe)
    data = serializer(recipe).data
    return Response(data, status=status.HTTP_201_CREATED)
