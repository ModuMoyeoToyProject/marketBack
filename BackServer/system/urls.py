from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('mapdata', views.map_data),
    path('scriptdata', views.script_data)
]