from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from petstagram.accounts.managers import AppUserManager
# Create your models here.


class AppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True, null=False, blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    objects = AppUserManager()



class Profile(models.Model):
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(blank=True, null = True, max_length=30)
    last_name = models.CharField(blank=True, null = True,  max_length=30)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_picture = models.URLField(blank=True, null=True)

    def get_full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'.strip()

        return 'Anonymous User'



