from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response

from recipes.models import Recipe


def post_obj(request, pk, model, serializer):
    recipe = get_object_or_404(Recipe, pk=pk)
    if model.objects.filter(user=request.user, recipe=recipe).exists():
        return Response(
            {'errors': 'Рецепт уже был добавлен'},
            status=status.HTTP_400_BAD_REQUEST,
        )
    model.objects.get_or_create(user=request.user, recipe=recipe)
    data = serializer(recipe).data
    return Response(data, status=status.HTTP_201_CREATED)


def delete_obj(request, pk, model):
    recipe = get_object_or_404(Recipe, pk=pk)
    if model.objects.filter(user=request.user, recipe=recipe).exists():
        follow = get_object_or_404(model, user=request.user, recipe=recipe)
        follow.delete()
        return Response(
            'Рецепт успешно удален',
            status=status.HTTP_204_NO_CONTENT
        )
    return Response(
        {'errors': 'Нельзя удалить то, чего нет'},
        status=status.HTTP_400_BAD_REQUEST
    )
