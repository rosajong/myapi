from rest_framework import serializers
from recipes.serializers import RecipeSerializer
from .models import Author


class AuthorSerializer(serializers.ModelSerializer):
    recipes = RecipeSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['full_name', 'recipes']
