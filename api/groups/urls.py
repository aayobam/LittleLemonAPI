from django.urls import path
from .import views


urlpatterns = [
    path('add-user/', views.AddUserToGroupView.as_view(), name='add_user_to_group'),
    path('<int:pk>/users/', views.ListGroupUsersView.as_view(), name='list_all_users_per_group'),
    path('groups/<int:pk>/users/<int:user_id>/', views.ListGroupUsersView.as_view(), name='delete_user_from_group'),
]
