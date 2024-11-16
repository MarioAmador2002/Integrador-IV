from django.db import models
"""
Pacientes
"""
class Pacientes(models.Model):
    Codigo = models.CharField(verbose_name="Codigo", max_length=5, unique=True)
    Nombres = models.CharField(verbose_name="Nombres", max_length=60)
    Apellidos = models.CharField(verbose_name="Apellidos", max_length=60)
    FecNacimiento = models.DateField(verbose_name='FecNacimiento')
    Direccion = models.CharField(verbose_name="Direccion", max_length=60)
    Telefono = models.CharField(verbose_name="Telefono", max_length=60)

    class Meta:
        verbose_name_plural = 'Pacientes'

    def __str__(self):
        return f'{self.Codigo} {self.Nombres}-{self.Apellidos}-{self.FecNacimiento}-{self.Direccion}-{self.Telefono}'
# Create your models here.
