from django.db import models
from apps.Catalogos.Pacientes.models import Pacientes
from apps.Modulo_Examen.Examen.models import Examen
from apps.Modulo_Medicamento.Medicamento.models import Medicamento
from apps.Catalogos.Medicos.models import Medicos
"""
Citas
"""
class Citas(models.Model):
    Num_citas = models.CharField(verbose_name='Num_citas',max_length=50)
    Fecha = models.DateField(verbose_name='Fecha',auto_now_add=True)
    Razon = models.CharField(verbose_name='Razon', max_length=50)
    Estado = models.CharField(verbose_name='Estado', max_length=50)
    Costo = models.CharField(verbose_name='Costo', max_length=50)
    paciente = models.ForeignKey(Pacientes, verbose_name='Pacientes', on_delete=models.PROTECT)
    examen = models.ForeignKey(Examen, verbose_name='Examen', on_delete=models.PROTECT)
    medicamento = models.ForeignKey(Medicamento,verbose_name='Medicamento', on_delete=models.PROTECT)
    medicos = models.ForeignKey(Medicos,verbose_name='Medicos', on_delete=models.PROTECT)
    class Meta:
        verbose_name_plural = 'Citas'

    def __str__(self):
        return f'{self.Num_citas} - {self.Fecha} - {self.Razon} - {self.Estado} - {self.Costo}'


"""
DetalleCitas
"""
class DetalleCitas(models.Model):
    Diagnostico = models.CharField(max_length=100)
    Tratamiento = models.CharField(max_length=100)
    citas = models.ForeignKey(Citas, related_name='DetalleCitas', on_delete=models.PROTECT)
    class Meta:
        verbose_name_plural = 'DetalleCitas'

    def __str__(self):
        return f'{self.Diagnostico}-{self.Tratamiento}'


