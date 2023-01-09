from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import *


class MapAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'description', 'width', 'height', 'required_level', 'coordinate', 'street']
    search_fields = ['name']
    class GarnishArrangementInline(admin.TabularInline):
        model=GarnishArrangement
        extra=0
        autocomplete_fields = ['garnish']
        verbose_name = '장식물 배치'
        verbose_name_plural = verbose_name
    inlines = [GarnishArrangementInline]
    autocomplete_fields = ['east_map', 'west_map', 'south_map', 'north_map']

    class Media:
        css = {
            'all': ('admin/css/custom.css',)
        }
    print(Media().css)

class MaptypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
class GarnishAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

admin.site.register(Map, MapAdmin)
admin.site.register(Maptype, MaptypeAdmin)
admin.site.register(Garnish, GarnishAdmin)