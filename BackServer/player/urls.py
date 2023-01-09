from django.contrib import admin
from django.urls import path, include
from .views import *
from . import views

urlpatterns = [
    path('', PlayerView.as_view()),
    path('action/hunting', views.player_hunting),
    path('action/harvesting', views.player_harvesting),
    path('action/taming', views.player_taming),
    path('action/farming', views.player_farming),
    path('action/fishing', views.player_fishing),
    path('action/buying', views.player_buying),
    path('action/selling', views.player_selling)
]