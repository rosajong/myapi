from __future__ import unicode_literals
from django.db import models
from django.contrib.contenttypes.models import ContentType
from cookbooks.models import Cookbook
from ingredients.models import Ingredient
from authors.models import Author


class Recipe(models.Model):
    name = models.CharField(max_length=128)
    author = models.ManyToManyField(Author, related_name='recipes')
    ingredients = models.ManyToManyField(Ingredient,
                                         related_name='recipes')
    cookbooks = models.ManyToManyField(Cookbook, related_name='recipes')

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'recipes'
