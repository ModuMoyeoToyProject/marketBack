from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('player/action/hunting', views.player_hunting),
    path('player/action/harvesting', views.player_harvesting),
    path('player/action/taming', views.player_taming),
    path('player/action/farming', views.player_farming),
    path('player/action/fishing', views.player_fishing)
]