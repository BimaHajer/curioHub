from django.db import models
import django.utils.timezone
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin,Permission
from django.contrib.auth.models import UserManager
from django.db import models




# # Create your models here.
class Role(models.Model):
    role_name=models.CharField(max_length=50)
    permissions=models.ManyToManyField(Permission)

    def __str__(self):
        if self.role_name:
            return self.role_name
        return super().__str__()

   

class userApp(AbstractBaseUser,models.Model):
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []
    first_name = models.TextField(null=False)
    last_name = models.TextField(null=False)
    username = models.CharField(unique=True, max_length=150)
    email = models.EmailField(null=False, unique=True)
    password = models.CharField(max_length=128, null=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    telephone = models.CharField(max_length=250, null=True)
    postal_code = models.IntegerField(null=True, blank=True)
    city = models.CharField(unique=True, max_length=150, blank=True, null=True)
    country = models.CharField(
        unique=True,
        max_length=150,
        blank=True,
        null=True)
    twitter = models.CharField(max_length=150, blank=True, null=True)
    instagram = models.CharField(max_length=150, blank=True, null=True)
    facebook = models.CharField(max_length=150, blank=True, null=True)
    date_joined = models.DateTimeField(default=django.utils.timezone.now)
    last_logout = models.DateTimeField(null=True)
    objects = UserManager()

    class Meta:
        db_table = "userApp"
