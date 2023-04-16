from django.contrib import admin
from .models import Order

@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display = ('user', 'delivery_crew', 'status', 'total')
    readonly_fields = ('id',)