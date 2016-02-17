from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Cookbook(models.Model):
    author = models.CharField(max_length=128)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'cookbooks'
