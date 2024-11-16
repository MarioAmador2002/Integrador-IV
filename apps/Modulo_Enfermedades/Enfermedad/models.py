from django.db import models

from apps.Catalogos.Pacientes.models import Pacientes

"""
Enfermedades
"""
class Enfermedad(models.Model):
    Nombre = models.CharField(verbose_name='Nombre', max_length=80)
    Descripcion = models.CharField(verbose_name='Descripcion', max_length=80)
    Sintomas = models.CharField(verbose_name='Sintoma', max_length=80)
    Tratamiento = models.CharField(verbose_name='Tratamientos', max_length=80)
    pacientes = models.ForeignKey(Pacientes, verbose_name='pacientes', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Enfermedad'

    def __str__(self):
        return f'{self.Nombre} - {self.Descripcion}- {self.Sintomas} - {self.Tratamiento}'

'''
DetalleEnfermedades
'''
class DetalleEnfermedades(models.Model):
    Tratamiento = models.CharField(verbose_name='tratamiento', max_length=50)
    Fecha_registro = models.CharField(verbose_name='fecha de registro', max_length=50)
    enfermedades = models.ForeignKey(Enfermedad, verbose_name='Enfermedad', on_delete=models.CASCADE)
    pacientes = models.ForeignKey(Pacientes, verbose_name='Pacientes', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'DetalleEnfermedades'

    def __str__(self):
        return f'{self.Tratamiento}- {self.Fecha_registro}'
