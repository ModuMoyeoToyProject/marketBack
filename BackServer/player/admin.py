from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import *
from db.models import *


class CharacterAdmin(admin.ModelAdmin):
    list_display = ['get_nickname', 'get_username', 'level', 'exp']
    
    @admin.display(ordering='user__nickname', description='닉네임')
    def get_nickname(self, obj):
        return obj.user.nickname

    @admin.display(ordering='user__username', description='사용자 이름')
    def get_username(self, obj):
        return obj.user.username

class InventoryAdmin(admin.ModelAdmin):
    list_display = ['get_nickname', 'usage', 'capacity']
     
    @admin.display(ordering='character__user__nickname', description='닉네임')
    def get_nickname(self, obj):
        return obj.character.user.nickname
    
    class ItemAmountInline(admin.TabularInline):
        model=ItemAmount
        extra=0
        autocomplete_fields = ['item']
        verbose_name = '보유 아이템'
        verbose_name_plural = verbose_name
    inlines = [ItemAmountInline]

class StatusAdmin(admin.ModelAdmin):
    list_display = ['get_nickname', 'hp', 'mp']
    
    @admin.display(ordering='user__nickname', description='닉네임')
    def get_nickname(self, obj):
        return obj.character.user.nickname

admin.site.register(Character, CharacterAdmin)
admin.site.register(Inventory, InventoryAdmin)
admin.site.register(Status,    StatusAdmin)
