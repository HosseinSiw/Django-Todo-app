from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from .managers import UserManager


class User(AbstractUser, PermissionsMixin):
    # Personal information fields
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255, null=True, blank=True)

    # Permissions and status fields
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Important dates fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.name
