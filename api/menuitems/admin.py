from django.contrib import admin
from .models import MenuItem


@admin.register(MenuItem)
class AdminMenuItem(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'category', 'featured')
