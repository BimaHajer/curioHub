from django.db import models
class Resume(models.Model):
    USERNAME_FIELD = "name"
    REQUIRED_FIELDS = []
    name = models.CharField(unique=True, max_length=150)
    description = models.CharField(max_length=128, null=True)
    skills=models.CharField(max_length=128, null=True)
    experience=models.CharField(max_length=128, null=True)
    education=models.CharField(max_length=128, null=True)
    fullname=models.CharField(max_length=128, null=True)
    titre=models.CharField(max_length=128, null=True)
    create_at=models.BooleanField(default=False)
    update_at=models.BooleanField(default=False)
    create_by=models.BooleanField(default=False)
    update_by=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
class Meta:
    db_table = 'resume'

# Create your models here.
