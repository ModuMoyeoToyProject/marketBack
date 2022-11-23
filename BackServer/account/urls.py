from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('register', views.register),
    path('login', views.login)
]