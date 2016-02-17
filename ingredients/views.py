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


# class IngredientFilter(django_filters.FilterSet):
#     class Meta:
#         model = Ingredient
#         fields = ['vegan', 'name']
#
#
# class IngredientListView(generics.ListAPIView):
#     queryset = Ingredient.objects.all()
#     serializer_class = IngredientSerializer
#     filter_backends = (filters.SearchFilter,)
#     search_fields = 'name'

    # class Meta:
    #     model = Ingredient
    #     fields = ['vegan']
