from django.contrib import admin

from apps.Catalogos.Medicos.models import Medicos

@admin.register(Medicos)
class MedicoAdmin(admin.ModelAdmin):
    search_fields = ['id,','Codigo']
    list_display = ['Codigo', 'Nombres','Apellidos','FecNacimiento','Direccion','Especialidad','Telefono']
# Register your models here.

