from django.contrib import admin
from apps.Modulo_Enfermedades.TipoEnfermedades.models import TipoEnfermedades

@admin.register(TipoEnfermedades)
class TipoEnfermedadesAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ['NombreTipo','Descripcion']
# Register your models here.
