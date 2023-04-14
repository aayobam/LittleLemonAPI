from django.contrib import admin
from .models import Cart


@admin.register(Cart)
class AdminCart(admin.ModelAdmin):
    list_display = ('user', 'menuitem', 'quantity', 'unit_price', 'price')
    readonly_fields = ('unit_price', 'price')
