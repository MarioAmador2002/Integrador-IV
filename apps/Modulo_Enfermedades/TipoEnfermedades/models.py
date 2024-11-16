from django.db import models
from apps.Modulo_Enfermedades.Enfermedad.models import Enfermedad

'''
TipoEnfermedades
'''
class TipoEnfermedades(models.Model):
    NombreTipo = models.CharField(verbose_name='NombreTipo',max_length=100)
    Descripcion = models.CharField(verbose_name='Descripcion',max_length=100)

    enfermedad = models.ForeignKey(Enfermedad, verbose_name='Enfermedad', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'TiposEnfermedades'

    def __str__(self):
        return f'{self.NombreTipo}-{self.Descripcion}'
# Create your models here.
