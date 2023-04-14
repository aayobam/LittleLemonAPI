from .models import Category
from rest_framework import generics
from .serializers import CategorySerializer
from api.common.throttles import CustomUserThrottle
from rest_framework.permissions import IsAuthenticated, IsAdminUser



class CreateCategoryView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    throttle_classes = [CustomUserThrottle]


class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    lookup_field = "id"
    lookup_url_kwarg = "category_id"


class UpdateCategoryView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    lookup_field = "id"
    lookup_url_kwarg = "category_id"


class DeleteCategoryView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    lookup_field = "id"
    lookup_url_kwarg = "category_id"
