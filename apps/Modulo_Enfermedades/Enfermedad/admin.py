from django.contrib import admin
from apps.Modulo_Enfermedades.Enfermedad.models import Enfermedad

@admin.register(Enfermedad)
class EnfermedadesAdmin(admin.ModelAdmin):
    search_fields = ['id','Nombre']
    list_display = ['Nombre','Descripcion','Sintomas','Tratamiento',]


