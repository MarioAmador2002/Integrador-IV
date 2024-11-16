from django.db import models
"""
Medicos
"""
class Medicos(models.Model):
    Codigo = models.CharField(verbose_name='Codigo', max_length=5, unique=True)
    Nombres = models.CharField(verbose_name='Nombres',max_length=50)
    Apellidos = models.CharField(verbose_name='Apellidos',max_length=50)
    FecNacimiento = models.DateField(verbose_name='FecNacimiento')
    Direccion = models.CharField(verbose_name='Direccion', max_length=50)
    Especialidad = models.CharField(verbose_name='Especialidad', max_length=50)
    Telefono = models.CharField(verbose_name='Telefono', max_length=20)

    class Meta:
        verbose_name_plural = 'Medicos'

    def __str__(self):
        return f'{self.Codigo}-{self.Nombres}-{self.Apellidos}-{self.FecNacimiento}-{self.Direccion}-{self.Especialidad}-{self.Telefono}'
# Create your models here.
