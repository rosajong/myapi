from django.shortcuts import render
from rest_framework import viewsets, generics, filters
from .models import Ingredient
from .serializers import IngredientSerializer
import django_filters


# Create your views here.
class IngredientViewSet(viewsets.ModelViewSet):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name', 'vegan')
