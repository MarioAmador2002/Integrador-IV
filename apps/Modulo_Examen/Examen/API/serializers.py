from django.db.migrations.serializer import Serializer
from rest_framework import serializers
from apps.Catalogos.Pacientes.models import Pacientes
from apps.Catalogos.Medicos.models import Medicos
from apps.Modulo_Examen.Examen.models import Examen, DetalleExamen

#Serializador para los detalles de los Examenes
class DetalleExamenSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleExamen
        fields = ['TipoExamen','Estado','Observacion']

#Serializador para los datos completos de un examen
class ExamenWithDetailsSerializer(serializers.ModelSerializer):
    paciente = serializers.SerializerMethodField()
    medicos = serializers.SerializerMethodField()
    DetalleExamen = DetalleExamenSerializer(many=True, read_only=True)

    class Meta:
        model = Examen
        fields = ['NumExamen', 'FecExamen', 'Resultado', 'Descripcion', 'paciente', 'medicos', 'DetalleExamen']

    def get_paciente(self, obj):
        paciente = obj.paciente
        return {
            "Codigo": paciente.Codigo,
            "Nombres": paciente.Nombres,
            "Apellidos": paciente.Apellidos,
            "FecNacimiento": paciente.FecNacimiento,
             "Direccion": paciente.Direccion,
             "Telefono": paciente.Telefono,
        }

    def get_medicos(self, obj):
        medico = obj.medico
        return {
            "Codigo": medico.Codigo,
            "Nombres": medico.Nombres,
             "Apellidos": medico.Apellidos,
              "FecNacimiento": medico.FecNacimiento,
             "Direccion": medico.Direccion,
             "Especialidad": medico.Especialidad,
            "Telefono": medico.Telefono,
         }


#Serializador para la creación de examen (solo acepta id y detalles)
class ExamenCreateSerializer(serializers.ModelSerializer):
    paciente = serializers.IntegerField(write_only=True)  # Solo ID del paciente
    medico = serializers.IntegerField(write_only=True)  # Solo ID del médico
    DetalleExamen = DetalleExamenSerializer(many=True, write_only=True)

    class Meta:
        model = Examen
        fields = ['NumExamen', 'FecExamen', 'Resultado', 'Descripcion','paciente', 'medico', 'DetalleExamen']
