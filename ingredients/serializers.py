from rest_framework import serializers
from .models import Ingredient


# from recipes.serializers import RecipeSerializer


class IngredientSerializer(serializers.ModelSerializer):
    # recipes = RecipeSerializer(many=True, read_only=True)

    class Meta:
        model = Ingredient
        fields = ['name', 'vegan', 'recipes']


class SecondIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name']
