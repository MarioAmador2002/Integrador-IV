from django.db import models
from apps.Modulo_Citas.Citas.models import Citas
'''
EstadoCitas
'''
class EstadoCitas(models.Model):
    Estado =models.CharField(max_length=50)
    Descripcion =models.CharField(max_length=50)
    Fecha_Registro =models.DateField()

    citas = models.ForeignKey(Citas, verbose_name='Citas', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'EstadosCitas'

    def __str__(self):
        return f'{self.Estado }- {self.Descripcion }- {self.Fecha_Registro }'
# Create your models here.