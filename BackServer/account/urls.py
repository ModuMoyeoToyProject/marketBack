from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register),
    path('login/', views.login)
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)