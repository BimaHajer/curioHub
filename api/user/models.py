from django.db import models
from django.contrib.auth.models import Group,Permission
import uuid
from django.utils import timezone
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser




# Create your models here.
class Role(models.Model):
    role_name=models.CharField(max_length=50)
    permissions=models.ManyToManyField(Permission)

    def __str__(self):
        if self.role_name:
            return self.role_name
        return super().__str__()

   
class user(models.Model):
    user_id=models.UUIDField(unique=True,editable=False,default=uuid.uuid4,verbose_name='Public identifier')
    email=models.EmailField(unique=True)
    username=models.CharField(max_length=30,default='')
    first_name=models.CharField(max_length=30,blank=True)
    last_name=models.CharField(max_length=30,blank=True)
    date_of_birth=models.DateTimeField(default=timezone.now)
    backup_email=models.EmailField(blank=True)
    phone_number=models.CharField(max_length=30,blank=True)
    date_joined=models.DateTimeField(default=timezone.now)
    is_active=models.BooleanField(default=True)
    is_recongnized=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)
    is_superusr=models.BooleanField(default=True)
    is_deleted=models.BooleanField(default=True)
    created_data=models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True)
    created_by=models.EmailField(default='system')
    mofified_by=models.EmailField(default='system')
    availability=models.CharField(max_length=255,default="available")
    important=models.BooleanField(default=False)
    blocked=models.BooleanField(default=False)
    deleted=models.BooleanField(default=False)
    post=models.CharField(max_length=30,blank=True)
    about=models.CharField(max_length=255,blank=True)
    shared_media=models.FileField(upload_to='shared_media/',blanc=True,null=True)
    status_choices=[
        ('online','Online'),
        ('away','Away'),
        ('busy','Do not disturb'),
        ('offline','Offline'),
    ]
    status=models.CharField(max_length=10,choices=status_choices,default="Online")
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    



