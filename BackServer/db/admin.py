from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django_summernote.admin import SummernoteModelAdmin, SummernoteInlineModelAdmin
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

class ScriptAdmin(admin.ModelAdmin):
    list_display = ['title']
    
    class SentenceInline(admin.TabularInline, SummernoteInlineModelAdmin):
        model=Sentence
        ordering = ['order']
        extra=0
        verbose_name = '스크립트 목록'
        verbose_name_plural = verbose_name
    inlines = [SentenceInline]

class SentenceAdmin(SummernoteModelAdmin):
    list_display = ['speaker', 'text', 'captioning_elapsed_time']
    summernote_fields = ['text']
    search_fields = ['speaker', 'text']
    

admin.site.register(Skill,    SkillAdmin)
admin.site.register(Itemtype, ItemtypeAdmin)
admin.site.register(Item,     ItemAdmin)
admin.site.register(Job,      JobAdmin)
admin.site.register(Script,   ScriptAdmin)
admin.site.register(Sentence, SentenceAdmin)