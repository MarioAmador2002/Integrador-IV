from django.contrib import admin
from apps.Modulo_Citas.Citas.models import Citas, DetalleCitas


@admin.register(Citas)
class CitasAdmin(admin.ModelAdmin):
    search_fields = ['id,', 'Num_citas']
    list_display = ['Num_citas','Fecha','Razon','Estado','Costo',]


@admin.register(DetalleCitas)
class DetalleCitasAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ['Diagnostico','Tratamiento']