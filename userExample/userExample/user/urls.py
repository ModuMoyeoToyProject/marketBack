from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.user_register, name='userRegister'),
    path('userInfo/', views.display_user, name='userInfo')
]
