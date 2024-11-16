from django.db import models
from apps.Catalogos.Pacientes.models import Pacientes
from apps.Modulo_Enfermedades.Enfermedad.models import Enfermedad
"""
Medicamento
"""
class Medicamento(models.Model):
    Nombre = models.CharField(verbose_name="Nombre", max_length=50)
    Descripcion = models.CharField(verbose_name="Descripcion", max_length=50)
    NombreGenerico = models.CharField(verbose_name="NombreGenerico", max_length=50)
    Presentacion = models.CharField(verbose_name="Presentacion", max_length=50)
    Contradicciones = models.CharField(verbose_name="Contradicciones", max_length=50)
    EfectosSecundarios = models.CharField(verbose_name="EfectosSecundarios", max_length=50)

    class Meta:
        verbose_name_plural = "Medicamentos"

    def __str__(self):
        return f' {self.Nombre}-{self.Descripcion}-{self.NombreGenerico}-{self.Presentacion}-{self.Contradicciones}-{self.EfectosSecundarios}'

"""
Medicamento
"""

class DetalleMedicamento(models.Model):
    Receta = models.CharField(max_length=100)
    Dosis = models.CharField(max_length=100)
    Frecuencia = models.CharField(max_length=100)
    Duracion = models.CharField(max_length=100)
    Indicacion = models.CharField(max_length=100)
    medicamento = models.ForeignKey(Medicamento, verbose_name='Medicamento', on_delete=models.CASCADE)
    pacientes = models.ForeignKey(Pacientes, verbose_name='Pacientes', on_delete=models.CASCADE)
    enfermedad = models.ForeignKey(Enfermedad, verbose_name='Enfermedad', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'DetalleMedicamentos'

    def __str__(self):
        return f'{self.Receta} {self.Dosis} {self.Frecuencia}-{self.Duracion}-{self.Indicacion}'
