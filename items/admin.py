from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemsAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price']
