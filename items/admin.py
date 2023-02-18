from django.contrib import admin
from .models import Items

@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price']
