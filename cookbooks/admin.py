from django.contrib import admin
from .models import Cookbook


# Register your models here.
@admin.register(Cookbook)
class CookbookAdmin(admin.ModelAdmin):
    pass
