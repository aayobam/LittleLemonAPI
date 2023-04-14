from .models import Category
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    class Meta:
        model = Category
        fields = ["id", "slug", "title"]