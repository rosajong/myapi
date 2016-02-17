from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CookbookSerializer
from .models import Cookbook


# Create your views here.
class CookbookViewSet(viewsets.ModelViewSet):
    serializer_class = CookbookSerializer
    queryset = Cookbook.objects.all()

