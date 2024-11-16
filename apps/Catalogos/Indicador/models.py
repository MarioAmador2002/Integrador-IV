from django.db import models
from apps.Modulo_Examen.Examen.models import Examen
"""
Indicador
"""
class Indicador(models.Model):
    Nombres = models.CharField(verbose_name='Nombres',max_length=60)
    UnidadMedida =models.CharField(verbose_name='UnidadMedida',max_length=60)
    ValorReferenciaMax = models.CharField(verbose_name='ValorReferenciaMax',max_length=60)
    ValorReferenciaMin = models.CharField(verbose_name='ValorReferenciaMin',max_length=60)
    Descripcion = models.CharField(verbose_name='Descripcion',max_length=60)

    examen = models.ForeignKey(Examen, verbose_name='Examen', on_delete=models.CASCADE)


    class Meta:
        verbose_name_plural = 'Indicador'

    def __str__(self):
        return f'{self.Nombres}-{self.UnidadMedida}-{self.ValorReferenciaMax}-{self.ValorReferenciaMin}-{self.Descripcion}'
# Create your models here.
