from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile


class CustomUserAdmin(UserAdmin):
    list_display = ("email", 'username', "is_active", "is_staff", "is_superuser")
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    search_fields = ('username', "email")
    ordering = ('email',)

    # Editing field sets
    fieldsets = (
        ("Personal", {"fields": ("email", "username", "password",)}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
    )
    # Add a new user fieldsets
    add_fieldsets = (
        ("Personal", {"fields": ("email", "username", "password1", "password2")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
    )


admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)

