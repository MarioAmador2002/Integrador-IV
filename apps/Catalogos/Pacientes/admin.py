from django.contrib import admin



from apps.Catalogos.Pacientes.models import Pacientes

@admin.register(Pacientes)
class PacientesAdmin(admin.ModelAdmin):
    search_fields = ['id,','Codigo']
    list_display = ['Codigo','Nombres','Apellidos','FecNacimiento','Direccion','Telefono']
# Register your models here.
