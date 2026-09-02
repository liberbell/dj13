from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from mysite.models import User

# Register your models here.
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {
            "fields": (
                "email",
                "password",
            )
        }),
        (None, {
            "fields": (
                "is_active",
            )
        })
    )