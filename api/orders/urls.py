from django.urls import path
from .import views


urlpatterns = [
    path('list', views.OrderListView.as_view(), name="view_orders"),
    path("detail/<uuid:order_id>", views.OrderDetailView.as_view(), name="order_detail"),
    path("add-delivery-crew-to-order", views.AddDeliveryCrewToOrderView.as_view(), name="add_delivery_crew_to_order"),
    path('update/<uuid:order_id>',views.UpdateOrderDeliveryStatusView.as_view(), name="update_order"),
    path('delete/<uuid:order_id>',views.DeleteOrderView.as_view(), name="delete_order")
]
