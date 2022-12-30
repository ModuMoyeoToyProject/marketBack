from django.contrib.auth.models import Group as Django_Group
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import *
from django.utils.translation import gettext_lazy as _


class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {
            "fields": (
                "nickname",
                "email",
                "gender",
                "picture",
                "status_message",
        ),},),
        (_("Permissions"), {
            "fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
        ),},),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {"fields": ("username", "password1", "password2")}),
        (_("Personal info"), {
            "fields": (
                "nickname",
                "email",
                "gender",
                "picture",
                "status_message",
        ),},),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ("username", "nickname", "email", "is_staff")
    search_fields = ("username", "nickname", "email")
    ordering = ("is_staff", "username",)

admin.site.register(User, UserAdmin)
admin.site.unregister(Django_Group)
admin.site.register(Group)
admin.site.register(Account)
