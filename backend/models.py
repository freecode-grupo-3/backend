from pydoc import describe
from django.db import models

# Create your models here.

class Disease(models.Model):

    name = models.CharField(max_length=64, unique=True, verbose_name="Name of the disease")
    description = models.CharField(max_length=512, verbose_name="Description of the disease")

    def __str__(self) -> str:
        return f"Disease: {self.name}"

class ReferenceType(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name="Reference type name")
    description = models.CharField(max_length=512, verbose_name="Description of the reference type")
