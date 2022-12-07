from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('action/hunting', views.player_hunting),
    path('action/harvesting', views.player_harvesting),
    path('action/taming', views.player_taming),
    path('action/farming', views.player_farming),
    path('action/fishing', views.player_fishing)
]