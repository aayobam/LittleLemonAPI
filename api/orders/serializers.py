from api.orderitems.models import OrderItem
from .models import Order
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field="username", queryset=Order.objects.all())
    class Meta:
        model = Order
        fields = ["id", 'user', 'total', 'status', 'created_on']


class AddDeliveryCrewToOrderSerializer(serializers.ModelSerializer):
    delivery_crew = serializers.ReadOnlyField(source="delivery_crew")

    class Meta:
        model = Order
        fields = ["id", 'delivery_crew', 'user', 'created_on', 'updated_on']


class UpdateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'status', 'created_on', 'updated_on']


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['order', 'menuitem', 'unit_price', 'quantity', 'price']