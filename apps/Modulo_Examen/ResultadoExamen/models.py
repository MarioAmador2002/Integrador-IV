from django.db import models
from apps.Modulo_Examen.Examen.models import Examen

'''
ResultadosExamenes
'''
class ResultadoExamen(models.Model):
    valor = models.IntegerField()
    Unidad = models.IntegerField()
    Interpretacion = models.IntegerField()
    FecResultado =models.IntegerField()

    examen = models.ForeignKey(Examen, verbose_name='Examen', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'ResultadosExamenes'

    def __str__(self):
        return f'{self.valor}-{self.Unidad}-{self.Interpretacion}-{self.FecResultado}'

