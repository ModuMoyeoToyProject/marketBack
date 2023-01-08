from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import *


class MapAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'required_level', 'coordinate', 'street']

admin.site.register(Map, MapAdmin)