from django.contrib import admin
from apps.Modulo_Examen.ResultadoExamen.models import ResultadoExamen


@admin.register(ResultadoExamen)
class ResultadoExamenAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ('valor','Unidad','Interpretacion','FecResultado')
# Register your models here.
