from django.db import models
class App(models.Model):
    id = models.UUIDField(unique=True, primary_key=True,)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = ['email']
    REQUIRED_FIELDS = ['email']
class Meta:
    db_table = 'App'

# Create your models here.
