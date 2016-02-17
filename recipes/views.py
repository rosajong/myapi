from django.shortcuts import render
from .models import Recipe
from rest_framework import viewsets
from .serializers import RecipeSerializer
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route


def home(request):

    return render(request, 'recipes/index.html', {'recipes': Recipe.objects.all()}) #TODO make sure this doesn't show all recipes but just the homepage instead.


# Create your views here.
class RecipeViewSet(viewsets.ModelViewSet):
    """
    ViewSet for listing, adding & changing Recipes
    """
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()

    # TODO make function with ingredients.
