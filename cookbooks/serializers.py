from rest_framework import serializers
from .models import Cookbook
from recipes.serializers import RecipeSerializer


class CookbookSerializer(serializers.ModelSerializer):
    recipes = RecipeSerializer(many=True, read_only=True)

    class Meta:
        model = Cookbook
        fields = ['author', 'recipes', 'name']
