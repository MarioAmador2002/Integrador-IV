from rest_framework.serializers import ModelSerializer
from apps.Modulo_Examen.Examen.models import Examen,DetalleExamen
from apps.Catalogos.Pacientes.API.serializers import PacientesSerializer
from apps.Catalogos.Medicos.API.serializers import MedicosSerializer
from rest_framework import serializers

"""
serializador de la clase DetalleExamen
"""
class DetalleExamenSerializer(ModelSerializer):
    paciente = PacientesSerializer(read_only=True)
    class Meta:
        model = DetalleExamen
        fields = ['TipoExamen','Estado','Observacion','paciente']


class ExamenSerializer(serializers.ModelSerializer):
    paciente = PacientesSerializer(read_only=True)
    medico = MedicosSerializer(read_only=True)
    detalle = DetalleExamenSerializer(many=True, read_only=True, source='detalleexamen_set')
    class Meta:
        model = Examen
        fields = ['NumExamen', 'FecExamen', 'Resultado', 'Descripcion', 'paciente', 'medico', 'detalle']


