from django.urls import path
from .import views


urlpatterns = [
    path('view-orders', views.OrderListView.as_view(), name="view_orders"),
    path("add-delievry-crew-to-order/", views.AddDeliveryCrewToOrderView.as_view(), name="add_delivery_crew_to_order"),
    path('update/<uuid:order_id>',views.UpdateOrderView.as_view(), name="update_order")
]
