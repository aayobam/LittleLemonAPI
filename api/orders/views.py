from .models import Order
from api.orderitems.models import OrderItem
from rest_framework import generics, status
from rest_framework.response import Response
from api.common.permissions import SuperUserPermission, DeliveryCrewPermission, ManagerPermission, IsOwnerPermission
from .serializers import AddDeliveryCrewToOrderSerializer, OrderItemSerializer, OrderSerializer, UpdateOrderSerializer


class OrderListView(generics.ListAPIView):
    queryset = Order.objects.select_related('user').all()
    serializer_class = OrderSerializer
    permission_classes = [IsOwnerPermission | DeliveryCrewPermission | SuperUserPermission]

    def get(self, request):
        user = request.user
        if user.groups.filter(name__iexact="manager").exists() or user.is_superuser:
            order_items = OrderItem.objects.all()
            serializer = OrderItemSerializer(order_items, many=True)
            if serializer.data == []:
                return Response({"message": "There are no orders available."}, status=status.HTTP_200_OK)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        elif request.user.groups.filter(name__iexact="delivery crew").exists():
            order_items = OrderItem.objects.filter(order__delivery_crew=user)
            serializer = OrderItemSerializer(order_items, many=True)
            if serializer.data == []:
                return Response({"message": "There are no orders available."}, status=status.HTTP_200_OK)
            return Response(serializer.data, status=status.HTTP_200_OK)
            
        order = self.queryset.filter(user=request.user)
        serializer = self.serializer_class(order, many=True)
        if serializer.data == []:
            return Response({"message": "You have no order."}, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class OrderDetailView(generics.RetrieveAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsOwnerPermission]
    lookup_field = 'id'
    lookup_url_kwarg = 'order_id'

    def get(self, request, *args, **kwargs):
        order_id = kwargs.get("order_id", None)
        if order_id is not None:
            order_items = OrderItem.objects.filter(order_id=order_id)
            if not order_items:
                return Response({"message":"there is no record associated with the order detail provided"}, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(order_items, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message":"Order id required."},status=status.HTTP_404_NOT_FOUND)
    

class AddDeliveryCrewToOrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = AddDeliveryCrewToOrderSerializer
    permission_classes = [ManagerPermission]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        order_id = serializer.validated_data.get("id", None)
        delivery_crew = serializer.validated_data.get('delivery_crew', None)
        order_obj = self.queryset.get(id=str(order_id).strip())
        if order_obj is not None:
            order_obj.delivery_crew = delivery_crew
            order_obj.save()
            return Response({"message":"Order updated."}, status=status.HTTP_200_OK)
        return Response({"message":"Order not found"}, status=status.HTTP_404_NOT_FOUND)


class UpdateOrderDeliveryStatusView(generics.RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = UpdateOrderSerializer
    permission_classes = [DeliveryCrewPermission | ManagerPermission]
    lookup_field = 'id'
    lookup_url_kwarg = "order_id"


class DeleteOrderView(generics.RetrieveDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = UpdateOrderSerializer
    permission_classes = [ManagerPermission]
    lookup_field = 'id'
    lookup_url_kwarg = "order_id"