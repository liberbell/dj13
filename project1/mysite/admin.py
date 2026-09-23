from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from mysite.models.account_models import User
from mysite.models.profile_models import Profile
from mysite.forms import UserCreationForm

# Register your models here.
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    
class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)
    
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
                "is_admin",
            )
        })
    )
    
    list_display = ("email", "is_active", "is_admin")
    list_filter = ()
    ordering = ()
    filter_horizontal = ()
    add_fieldsets = (
        (None, {
            'fields': ('email', 'password',),
        }),
    )
    
    add_form = UserCreationForm
    inlines = (ProfileInline,)
    
admin.site.register(User, CustomUserAdmin)
admin.site.unregister(Group)