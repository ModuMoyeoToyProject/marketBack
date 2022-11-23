from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('account/', include('account.urls')),
    path('admin/', admin.site.urls),
    path('game/system/', include('system.urls')),
    path('game/player/', include('player.urls')),
]
