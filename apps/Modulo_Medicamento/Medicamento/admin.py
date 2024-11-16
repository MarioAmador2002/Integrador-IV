from django.contrib import admin
from apps.Modulo_Medicamento.Medicamento.models import Medicamento

@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    search_fields = ['id', 'Nombre']
    list_display = ['Nombre', 'Descripcion','NombreGenerico','Presentacion','Contradicciones','EfectosSecundarios',]
