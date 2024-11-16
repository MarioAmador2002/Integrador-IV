from django.db import models

from apps.Catalogos.Pacientes.models import Pacientes

"""
Genero
"""
class Genero(models.Model):
    Descripcion =  models.CharField(verbose_name='Descripcion',max_length=60)

    pacientes = models.ForeignKey(Pacientes, verbose_name='Pacientes', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Genero'

    def __str__(self):
        return f'{self.Descripcion}'

# Create your models here.
