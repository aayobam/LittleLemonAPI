from .models import Order
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ["id", 'total', 'status', 'created_on']


class AddDeliveryCrewToOrderSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    total = serializers.ReadOnlyField()
    status = serializers.ReadOnlyField()
    created_on = serializers.ReadOnlyField()
    updated_on = serializers.ReadOnlyField()
    class Meta:
        model = Order
        fields = ["id", 'delivery_crew', 'total', 'status', 'created_on', 'updated_on']


class UpdateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'status', 'created_on', 'updated_on']