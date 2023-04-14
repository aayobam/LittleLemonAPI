from django.urls import path
from .import views


urlpatterns = [
    path('create-cart', views.AddItemsToCartView.as_view(), name="create_cart"),
    path('view-cart', views.ViewCartItems.as_view(), name="view_cart"),
    path('checkout', views.CheckoutView.as_view(), name="checkout")
]
