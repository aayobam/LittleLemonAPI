from django.urls import path
from .import views


urlpatterns = [
    path('create', views.CreateCategoryView.as_view(), name="create_category"),
    path('list', views.CategoryListView.as_view(), name="category_list"),
    path('detail/<uuid:category_id>', views.CategoryDetailView.as_view(), name="category_detail"),
    path('update/<uuid:category_id>', views.UpdateCategoryView.as_view(), name="update_category"),
    path('delete/<uuid:category_id>', views.DeleteCategoryView.as_view(), name="delete_category")
]
