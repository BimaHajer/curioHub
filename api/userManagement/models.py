from django.db import models
from django.contrib.auth.models import Group,Permission
import uuid
from django.utils import timezone
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser




# # Create your models here.
class Role(models.Model):
    role_name=models.CharField(max_length=50)
    permissions=models.ManyToManyField(Permission)

    def __str__(self):
        if self.role_name:
            return self.role_name
        return super().__str__()

   
class UserApp(AbstractBaseUser,models.Model):
    id = models.UUIDField(unique=True, primary_key=True, editable=False, default=uuid.uuid4, verbose_name='Public identifier')
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_of_birth = models.DateTimeField(default=timezone.now)
    backup_email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_recognized = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    created_by = models.EmailField(default='system')
    modified_by = models.EmailField(default='system')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    availability = models.CharField(max_length=255, default="available")
    important = models.BooleanField(default=False)
    blocked = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    post = models.CharField(max_length=30, blank=True)
    about = models.CharField(max_length=255, blank=True)
    status_choices = [
        ('online', 'Online'),
        ('away', 'Away'),
        ('busy', 'Do not disturb'),
        ('offline', 'Offline'),
    ]
    status = models.CharField(max_length=10, choices=status_choices, default="Online")

    USERNAME_FIELD = ['email','username']
    REQUIRED_FIELDS = ['email','username']
    class Meta:
        db_table = 'userapp'



