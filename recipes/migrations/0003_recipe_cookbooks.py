# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-08 22:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbooks', '0002_auto_20160108_2203'),
        ('recipes', '0002_recipe_ingredients'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='cookbooks',
            field=models.ManyToManyField(related_name='recipes', to='cookbooks.Cookbook'),
        ),
    ]
