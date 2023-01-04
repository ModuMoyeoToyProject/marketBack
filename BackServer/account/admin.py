from django.contrib.auth.models import Group as Django_Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib import admin
from .models import *
from django.utils.translation import gettext_lazy as _


# admin 페이지에 보여질 정보에 대한 분류 기준, 기존 UserAdmin을 상속받아 사용자정의
class UserAdmin(UserAdmin):
    fieldsets = ( # 계정 수정 페이지에 보여질 항목
        (None, {'fields': ('username', 'password')}), # 최상단에 보여질 필드
        (_('Personal info'), { # 개인정보 항목에 보여질 필드
            'fields': (
                'nickname',
                'email',
                'gender',
                'picture',
                'status_message',
        ),},),
        (_('Permissions'), { # 계정 권한 항목에 보여질 필드
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
        ),},),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = ( # 계정 추가 페이지에 보여질 항목
        (None, {'fields': ('username', 'password1', 'password2')}), # 최상단에 보여질 필드
        (_('Personal info'), { # 개인정보 항목에 보여질 필드
            'fields': (
                'nickname',
                'email',
                'gender',
                'picture',
                'status_message',
        ),},),
        (_('Permissions'), {# 계정 권한 항목에 보여질 필드
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
        ),},),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}), # 중요한 정보 항목에 보여질 필드
    )
    list_display = ['username', 'nickname', 'email', 'is_staff'] # admin 페이지의 계정 리스트에 보여질 컬럼
    search_fields = ['username', 'nickname', 'email'] # admin 페이지의 검색창의 검색 대상
    ordering = ['is_staff', 'username',] # admin 페이지에서 계정 목록의 정렬 기준

class GroupAdmin(GroupAdmin):
    filter_horizontal=('permissions',)

admin.site.register(User, UserAdmin) # User 계정을 admin 페이지에 등록
admin.site.unregister(Django_Group) # Default Group 엔티티를 admin 페이지에서 제거
admin.site.register(Group, GroupAdmin) # Group 계정을 admin 페이지에 등록, User와 동일한 위치에 두기 위해서 재등록
