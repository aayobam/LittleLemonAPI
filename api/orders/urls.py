from django.urls import path
from .import views


urlpatterns = [
    path('apiview', views.api_view, name="api_view")
]
