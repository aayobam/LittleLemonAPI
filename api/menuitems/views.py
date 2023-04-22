from .models import MenuItem
from rest_framework import generics
from .serializers import MenuItemSerializer
from api.common.filters import MenuItemFilter
from rest_framework.filters import SearchFilter
from api.common.throttles import CustomUserThrottle
from api.common.permissions import ManagerPermission
from django_filters.rest_framework import DjangoFilterBackend


class CreateMenuItemView(generics.CreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [ManagerPermission]


class MenuItemListView(generics.ListAPIView):
    queryset = MenuItem.objects.select_related('category').all()
    serializer_class = MenuItemSerializer
    filterset_class = MenuItemFilter
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['category__title', 'price', 'title']
    throttle_classes = [CustomUserThrottle]


class MenuItemDetailView(generics.RetrieveAPIView):
    queryset = MenuItem.objects.select_related('category').all()
    serializer_class = MenuItemSerializer
    lookup_field = "id"
    lookup_url_kwarg = "menuitem_id"


class UpdateMenuItemView(generics.UpdateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [ManagerPermission]
    lookup_field = "id"
    lookup_url_kwarg = "menuitem_id"


class DeleteMenuItemView(generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [ManagerPermission]
    lookup_field = "id"
    lookup_url_kwarg = "menuitem_id"
