import email
from django.db import models
from django.contrib.auth.models import AbstractUser
from backend.models import Disease, ReferenceType
# Create your models here.

class User(AbstractUser):
    email = models.EmailField('email address', unique=True)
    diseases_of_interest = models.ManyToManyField(to=Disease, related_name='+')
    reference_types_of_interest = models.ManyToManyField(to=ReferenceType, related_name='+')
