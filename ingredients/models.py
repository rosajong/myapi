from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=64)
    vegan = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    # @staticmethod
    # def check_if_vegan(self, vegan):
    #     if vegan:
    #         print("This ingredient is vegan")
    #     else:
    #         print("This shit ain't vegan")
    #
    # @staticmethod
    # def show_me_them_vegan_ingredients(self, vegan):
    #     vegan_ingredients = filter(vegan=True)
    #     return vegan_ingredients

    class Meta:
        app_label = 'ingredients'
