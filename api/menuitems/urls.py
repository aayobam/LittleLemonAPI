from django.urls import path
from .import views


urlpatterns = [
    path('create', views.CreateMenuItemView.as_view(), name="create_menuitem"),
    path('list', views.MenuItemListView.as_view(), name="menuitem_list"),
    path('detail/<uuid:menuitem_id>', views.MenuItemDetailView.as_view(), name="menuitem_detail"),
    path('update/<uuid:menuitem_id>', views.UpdateMenuItemView.as_view(), name="update_menuitem"),
    path('delete/<uuid:menuitem_id>', views.DeleteMenuItemView.as_view(), name="delete_menuitem")
]
