from .models import MenuItem
from rest_framework import serializers
from api.categories.serializers import CategorySerializer


class MenuItemSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    category = CategorySerializer(read_only=True)
    
    class Meta:
        model = MenuItem
        fields = ["id", "category", "title", 'price', 'featured']