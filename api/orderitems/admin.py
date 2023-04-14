from django.contrib import admin

from api.orderitems.models import OrderItem


@admin.register(OrderItem)
class AdminOrderItem(admin.ModelAdmin):
    list_display = ('order', 'menuitem', 'quantity', 'unit_price', 'price')