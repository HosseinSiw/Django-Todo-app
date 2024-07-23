from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("email", "is_active", "is_staff", "is_superuser")
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    search_fields = ('name', "email")

    # Editing field sets
    fieldsets = (
        ("Personal", {"fields": ("email", "name")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
    )
    # Add a new user fieldsets
    add_fieldsets = (
        ("Personal", {"fields": ("email", "name", "password1", "password2")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
    )


admin.site.register(User, CustomUserAdmin)

