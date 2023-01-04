from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import *


class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'hp_consumption', 'mp_consumption']

class ItemtypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'description', 'purchase_price', 'sell_price', 'weight', 'durability']
    search_fields = ['name']

class JobAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


admin.site.register(Skill,    SkillAdmin)
admin.site.register(Itemtype, ItemtypeAdmin)
admin.site.register(Item,     ItemAdmin)
admin.site.register(Job,      JobAdmin)