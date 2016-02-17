from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Author(models.Model):
    full_name = models.CharField(max_length=128)

    def __str__(self):
        return self.full_name

    class Meta:
        app_label = 'authors'

#blabla
