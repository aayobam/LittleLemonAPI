from decimal import Decimal
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from api.menuitems.models import MenuItem
from api.orderitems.models import OrderItem
from django.db import transaction
from api.orders.models import Order
from .models import Cart
from rest_framework import status, generics
from .serializers import CartSerializer, CheckoutSerializer, FetchCartSerializer
from rest_framework.views import APIView


class AddItemsToCartView(APIView):
    serializer_class = CartSerializer
    
    def get(self, request):
        queryset = Cart.objects.filter(user=request.user)
        serializer = FetchCartSerializer(queryset, many=True)
        if serializer.data == []:
            return Response({"message": "cart is empty."}, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={"request":request})
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ViewCartItems(APIView):
    serializer_class = CartSerializer
    
    def get(self, request):
        carts = Cart.objects.filter(user=self.request.user)
        serializer = FetchCartSerializer(carts, many=True)
        if serializer.data == []:
            return Response({"message": "cart is empty."}, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class CheckoutView(generics.GenericAPIView):
    queryset = Cart.objects.all()
    serializer_class = CheckoutSerializer

    def get(self, request):
        queryset = self.queryset.filter(user=request.user)
        serializer = FetchCartSerializer(queryset, many=True)
        if serializer.data == []:
            return Response({"message": "There is no item in cart."}, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @transaction.atomic
    def post(self, request):
        queryset = self.queryset.filter(user=request.user)
        serializer = FetchCartSerializer(queryset, many=True, context={"request":request})

        if serializer.data == []:
            return Response({"message": "There is no item in cart."}, status=status.HTTP_200_OK)
        
        payloads = serializer.data
        cart_total = sum(Decimal(item["price"]) for item in payloads)
        order = Order.objects.create(user=request.user, status=1, total=cart_total)
        for item in payloads:
            unit_price = Decimal(item["unit_price"])
            price = Decimal(item["price"])
            item_obj = get_object_or_404(MenuItem, id=str(item["menuitem"]))
            if not item_obj:
                return Response({"message": "Item not found in stock"})
            order_items = OrderItem.objects.create(order=order, menuitem=item_obj, quantity=item["quantity"], unit_price=unit_price, price=price)
            order_items.save()

            # automatically clears the cart after saving order and order items.
            queryset.delete()
        return Response({"message": "Order placed successfully"}, status=status.HTTP_201_CREATED)
    
    
