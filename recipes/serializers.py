from rest_framework import serializers
from .models import Recipe
from ingredients.serializers import SecondIngredientSerializer


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = SecondIngredientSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ['name', 'author', 'ingredients', 'cookbooks']
