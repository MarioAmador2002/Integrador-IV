from django.contrib import admin
from apps.Catalogos.Indicador.models import Indicador

@admin.register(Indicador)
class IndicadorAdmin(admin.ModelAdmin):
    search_fields = ['id', 'Nombres']
    list_display = ['Nombres', 'UnidadMedida','ValorReferenciaMax','ValorReferenciaMin','Descripcion']

# Register your models here.