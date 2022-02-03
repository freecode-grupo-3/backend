import email
from django.db import models
from django.contrib.auth.models import AbstractUser
from backend.models import Disease
# Create your models here.

class User(AbstractUser):
    email = models.EmailField('email address', unique=True)
    disease_of_interest = models.ManyToManyField(to=Disease, related_name='+')
    # REQUIRED_FIELDS = ['username']
