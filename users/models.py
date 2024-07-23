from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractBaseUser, PermissionsMixin):
    """
    This class is a custom user model for our app.
    """
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

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Profile(models.Model):
    """
    This class represents the profile model to the db.
    """
    # The user of profile
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    # additional information
    img = models.ImageField(null=True, blank=True, upload_to='profile_pics')
    last_name = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()

    # How to represent a single
    def __str__(self):
        return f"{self.user.email} / {self.first_name}"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
