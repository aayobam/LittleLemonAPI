from .models import Category
from rest_framework import generics
from .serializers import CategorySerializer
from api.common.throttles import CustomUserThrottle
from api.common.permissions import ManagerPermission



class CreateCategoryView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [ManagerPermission]


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    throttle_classes = [CustomUserThrottle]


class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "id"
    lookup_url_kwarg = "category_id"


class UpdateCategoryView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [ManagerPermission]
    lookup_field = "id"
    lookup_url_kwarg = "category_id"


class DeleteCategoryView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [ManagerPermission]
    lookup_field = "id"
    lookup_url_kwarg = "category_id"
