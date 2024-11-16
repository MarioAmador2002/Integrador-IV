from django.db import models
from apps.Catalogos.Pacientes.models import Pacientes
from apps.Catalogos.Medicos.models import Medicos

"""
clase examen
"""
class Examen(models.Model):
    NumExamen = models.IntegerField(verbose_name='NumExamen')
    FecExamen = models.DateField(verbose_name='FecExamen')
    Resultado = models.CharField(verbose_name='Resultado', max_length=60)
    Descripcion = models.CharField(verbose_name='Descripcion', max_length=60)
    paciente = models.ForeignKey(Pacientes, verbose_name='Paciente', on_delete=models.PROTECT)
    medico = models.ForeignKey(Medicos, on_delete=models.PROTECT)
    class Meta:
        verbose_name_plural = 'Exámenes'

    def __str__(self):
        return f'{self.NumExamen} - {self.FecExamen} - {self.Resultado} - {self.Descripcion}'

"""
clase detalleexamen
"""
class DetalleExamen(models.Model):
    TipoExamen = models.CharField(verbose_name="TipoExamen", max_length=60)
    Estado = models.CharField(verbose_name="Estado", max_length=60)
    Costo = models.IntegerField(verbose_name="Costo", default=0)
    Observacion = models.CharField(verbose_name="Observacion", max_length=60)
    examen = models.ForeignKey(Examen, verbose_name='Examen', on_delete=models.PROTECT)
    class Meta:
        verbose_name_plural = "Detalleexamen"

    def __str__(self):
        return f'{self.TipoExamen} - {self.Estado} - {self.Costo} - {self.Observacion}'


