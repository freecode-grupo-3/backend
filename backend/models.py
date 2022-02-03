from abc import abstractclassmethod
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
    place_of_origin_name = models.CharField(max_length=100, verbose_name='Place of origin name', blank=True)
    address_of_place_of_origin = models.CharField(max_length=255, verbose_name='Address of the place of origin', blank=True)
    extra_info = models.CharField(max_length=500, verbose_name='Extra information for this reference', blank=True)


    def get_types(self):
        return [
            (lambda: self.medicinereference, MedicineReference.DoesNotExist, 'medicine'),
            (lambda: self.labtestreference, LabTestReference.DoesNotExist, 'lab-test'),
            (lambda: self.doctorreference, DoctorReference.DoesNotExist, 'doctor'),
        ]

    def type_of_reference(self):

        for t in self.get_types():
            try:
                t[0]()
                return t[2]
            except t[1]:
                pass

        raise 'other'

    @property
    def child(self):
        for t in self.get_types():
            try:
                return t[0]()
            except t[1]:
                pass
        return self

    def __str__(self) -> str:
        return str(self.child)

class PriceMixin(models.Model):
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Price of the medicine', null=True, blank=True)

    class Currency(models.TextChoices):
        USD = 'USD'
        VES = 'VES'

    currency = models.CharField(max_length=3, choices=Currency.choices, default=None, null=True, blank=True)

    class Meta:
        abstract = True

class MedicineReference(Reference, PriceMixin):
    name = models.CharField(max_length=100, verbose_name='Medicine name', blank=False)
    presentation = models.CharField(max_length=100, verbose_name='Presentation of the medicine', blank=True)

    def __str__(self):
        return 'Medicine: ' + self.name

class LabTestReference(Reference, PriceMixin):
    name = models.CharField(max_length=100, verbose_name='Medicine name', blank=False)
    who_runs_the_test = models.CharField(max_length=100, verbose_name='Who runs this lab test', blank=True)

    def __str__(self):
        return 'Lab test reference: ' + self.name

class DoctorReference(Reference, PriceMixin):
    name = models.CharField(max_length=100, verbose_name='Medicine name', blank=False)

    class Specialty(models.TextChoices):
        ONCOLOGY = 'ONCOLOGY'
        MASTOLOGY = 'MASTOLOGY'
        GINECOLOGY = 'GINECOLOGY'
        DERMATOLOGY = 'DERMATOLOGY'
        GASTROENTEROLOGY = 'GASTROENTEROLOGY'
        UROLOGY = 'UROLOGY'
        PNEUMONOLOGY = 'PNEUMONOLOGY'
        OTHER = 'OTHER'

    specialty = models.CharField(max_length=16, verbose_name='Specialty of the doctor', blank=False)
    contact_phone_number = models.CharField(max_length=20, verbose_name='Contact phone number', blank=False)

    def __str__(self):
        return 'Doctor: ' + self.name
