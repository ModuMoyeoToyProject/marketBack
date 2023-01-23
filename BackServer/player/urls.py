from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


# router = DefaultRouter()
# router.register(r'characters', CharacterViewSet)
# router.register(r'inventories', InventoryViewSet)


urlpatterns = [
    # path('', include(router.urls)),
    path('characters/', views.CharacterView.as_view()),
    # path('character', CharacterView.as_view()),
    # path('character', InventoryViewSet.as_view()),
    path('map', views.MapView.as_view()),
    path('action/hunting', views.player_hunting),
    path('action/harvesting', views.player_harvesting),
    path('action/taming', views.player_taming),
    path('action/farming', views.player_farming),
    path('action/fishing', views.player_fishing),
    path('action/buying', views.player_buying),
    path('action/selling', views.player_selling)
]