from django.urls import path, re_path
from . import views

urlpatterns = [
    path('REST_app/', views.rest_app, name='rest_app'),
    path('rest_list', views.rest_list, name='restaurant_list')
]
