from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    #path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api/carts/', include('api.carts.urls')),
    path('api/categories/', include('api.categories.urls')),
    path('api/groups/', include('api.groups.urls')),
    path('api/menuitems/', include('api.menuitems.urls')),
    path('api/orderitems/', include('api.orderitems.urls')),
    path('api/orders/', include('api.orders.urls')),
]
