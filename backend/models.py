from django.db import models

# Create your models here.


class Enfermedad(models.Model):

    name = models.CharField(max_length=64, unique=True, verbose_name="Nombre de la Enfermedad")
    description = models.CharField(max_length=512, verbose_name="Descripcion de la Enfermedad")
    
    def __str__(self) -> str:
        return f"Enfermedad: {self.name}"
