from django.contrib import admin
from apps.Modulo_Citas.EstadoCitas.models import EstadoCitas

@admin.register(EstadoCitas)
class EstadoCitasAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ['Estado','Descripcion','Fecha_Registro']
