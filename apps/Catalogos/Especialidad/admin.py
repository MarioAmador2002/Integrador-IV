from django.contrib import admin
from apps.Catalogos.Especialidad.models import Especialidad

@admin.register(Especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    search_fields = ['id', 'Nombre']
    list_display = ['Nombre', 'Descripcion','Estatus', 'Fecha','FechaModificacion',]

# Register your models here.