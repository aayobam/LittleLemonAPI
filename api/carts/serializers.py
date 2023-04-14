from .models import Cart
from decimal import Decimal
from rest_framework import serializers


class CartSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    quantity = serializers.IntegerField()

    class Meta:
        model = Cart
        fields = ['user', 'menuitem', 'quantity']
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=('user', 'menuitem'),
                message=("Item already exist in cart.")
            )
        ]
    
    def validate(self, data):
        quantity = data.get('quantity')
        menuitem = data.get('menuitem')
        print(f"ITEM IN SERIALIZER: {menuitem}")
        if quantity <= 0:
            raise serializers.ValidationError("quantity cannot be less than 1.")
        return data

    def get_item_price(cart:Cart):
        item_price = Decimal(cart.menuitem.price)
        return item_price
    
    def get_total_price(cart:Cart):
        total_price = Decimal(cart.menuitem.price) * cart.quantity
        return total_price
    
    def create(self, validated_data):
        cart = Cart.objects.create(**validated_data)
        return cart


class FetchCartSerializer(serializers.ModelSerializer):
    menuitem = serializers.ReadOnlyField(source="menuitem.id")
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Cart
        fields = ['user', 'menuitem', 'quantity', 'unit_price', 'price']

    def get_item_price(cart:Cart):
        item_price = Decimal(cart.menuitem.price)
        return item_price
    
    def get_total_price(cart:Cart):
        price = Decimal(cart.menuitem.price)
        total_price = price * cart.quantity
        return total_price
    
    def create(self, validated_data):
        cart = Cart.objects.create(**validated_data)
        return cart

 
class CheckoutSerializer(serializers.ModelSerializer):
    """
    This returns no form feed as data are been fetched from the cart table based
    on currently logged in user_id to place orders.
    """
    class Meta:
        model = Cart
        fields = ['id',]