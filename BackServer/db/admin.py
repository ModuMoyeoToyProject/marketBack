from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django_summernote.admin import SummernoteModelAdmin, SummernoteInlineModelAdmin
from .models import *


class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'hp_consumption', 'mp_consumption']

# class ItemstatAdmin(admin.ModelAdmin):
#     list_display = ['hp', 'mp', 'power']

class ItemtypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'description', 'image_path', 'purchase_price', 'sell_price', 'weight', 'hp', 'mp', 'power']
    search_fields = ['name']
    ordering = ['name']

    fieldsets = ( # 계정 수정 페이지에 보여질 항목
        (None, {
            'fields': (
                'name',
                'type',
                'description',
                'image_path',
                'weight',
        )}), # 최상단에 보여질 필드
        ('가격 정보', {
            'fields': (
                'purchase_price',
                'sell_price',
        ),},),
        ('부가 능력치', {
            'fields': (
                'hp',
                'mp',
                'power',
        ),},),
    )



class BuildingAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    filter_horizontal=('sale_items',)

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
# admin.site.register(Itemstat, ItemstatAdmin)
admin.site.register(Itemtype, ItemtypeAdmin)
admin.site.register(Item,     ItemAdmin)
admin.site.register(Building, BuildingAdmin)
admin.site.register(Job,      JobAdmin)
admin.site.register(Script,   ScriptAdmin)
admin.site.register(Sentence, SentenceAdmin)