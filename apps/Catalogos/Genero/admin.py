from django.contrib import admin
from apps.Catalogos.Genero.models import Genero

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ['Descripcion']

# Register your models here.
