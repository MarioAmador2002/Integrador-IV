from django.contrib import admin
from apps.Modulo_Examen.Examen.models import Examen, DetalleExamen


@admin.register(Examen)
class ExamenAdmin(admin.ModelAdmin):
    search_fields = ['id','NumExamen']
    list_display = ['NumExamen','FecExamen','Resultado','Descripcion']

@admin.register(DetalleExamen)
class DetalleExamenAdmin(admin.ModelAdmin):
    search_fields = ['id','TipoExamen']
    list_display = ['TipoExamen','Estado','Costo','Observacion']


