from django.shortcuts import get_object_or_404
from .models import Order
from .serializers import AddDeliveryCrewToOrderSerializer, OrderSerializer, UpdateOrderSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from api.common.permissions import DeliveryCrewPermission, ManagerPermission


class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request):
        queryset = self.queryset.filter(user=request.user)
        serializer = self.serializer_class(queryset, many=True)
        if serializer.data == []:
            return Response({"message": "You have no order."}, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class AddDeliveryCrewToOrderView(generics.RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = AddDeliveryCrewToOrderSerializer
    permission_classes = [IsAdminUser, ManagerPermission()]
    lookup_field = 'id'
    lookup_url_kwarg = "order_id"

    def get(self, request, order_id):
        queryset = get_object_or_404(Order, id=order_id)
        serializer = OrderSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateOrderView(generics.RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = UpdateOrderSerializer
    permission_classes = [IsAdminUser, ManagerPermission, DeliveryCrewPermission]
    lookup_field = 'id'
    lookup_url_kwarg = "order_id"

    def get_queryset(self):
        orders = self.queryset.filter(delivery_crew=self.request.user)
        return orders
    

    # def get(self, request):
    #     queryset = self.queryset.filter(delivery_crew=request.user)
    #     serializer = OrderSerializer(queryset)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    
    # def update(self, request, *args, **kwargs):
    #     order = get_object_or_404(Order, id=kwargs["order_id"])
    #     serializer = self.serializer_class(order)
    #     return Response(serializer.data, status=status.HTTP_200_OK)