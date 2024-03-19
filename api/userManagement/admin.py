from django.contrib import admin
from .models import UserApp
from userManagement import views
admin.site.register(UserApp)
# Register your models here.
