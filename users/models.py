import email
from django.db import models
from django.contrib.auth.models import AbstractUser
from backend.models import Enfermedad
# Create your models here.

class User(AbstractUser):
    email = models.EmailField('email address', unique=True)
    ills_of_interest = models.ManyToManyField(to=Enfermedad, related_name='+')
    # REQUIRED_FIELDS = ['username']
