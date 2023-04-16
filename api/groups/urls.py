from django.urls import path
from .import views


urlpatterns = [
    path('users/list', views.UserListView.as_view(), name='user_list'),
    path('create-group', views.GroupListCreateView.as_view(), name='group_list'),
    path('add-user-to-group', views.AddUserToGroupView.as_view(), name="add_user_to_group"),
    path('remove-user-from-group', views.RemoveUserFromGroupView.as_view(), name='remove_user_from_group'),
]
