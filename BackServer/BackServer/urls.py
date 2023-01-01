from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('account/', include('account.urls')),
    path('game/system/', include('system.urls')),
    path('game/player/', include('player.urls')),
    path('', admin.site.urls),
]
