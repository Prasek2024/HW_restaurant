from django.urls import path
from . import views

urlpatterns = [
    path('rest_app/', views.rest_app, name='rest_app'),
    path('rest_list/', views.rest_list, name='restaurant_list'),
    path("rest_users", views.rest_users, name="rest_users")
]
