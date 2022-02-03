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

class Reference(models.Model):
    created_at = models.DateTimeField(verbose_name='Created date', auto_now_add=True, blank=True)
    last_modified = models.DateTimeField(verbose_name='Last modified date', auto_now=True, blank=True)
    created_by = models.ForeignKey('users.User', null=True, blank=True, on_delete=models.SET_NULL)
    related_disease = models.ForeignKey(Disease, null=True, blank=True, on_delete=models.SET_NULL)
    place_of_origin_name = models.CharField(max_length=100, verbose_name='Place of origin name')
    address_of_place_of_origin = models.CharField(max_length=255, verbose_name='Address of the place of origin')

class MedicineReference(Reference):
    name = models.CharField(max_length=100, verbose_name='Medicine name', blank=False)
    presentation = models.CharField(max_length=100, verbose_name='Presentation of the medicine', blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Price of the medicine')

    class Currency(models.TextChoices):
        USD = 'USD'
        VES = 'VES'

    currency = models.CharField(max_length=3, choices=Currency.choices, default=None, null=True, blank=True)
