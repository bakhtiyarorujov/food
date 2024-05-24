from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    description = models.CharField(max_length=250, null=True, blank=True)
    profile_photo = models.ImageField(upload_to='user_profile', null=True, blank=True)