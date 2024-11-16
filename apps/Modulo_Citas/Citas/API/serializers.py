from rest_framework import serializers
from apps.Modulo_Citas.Citas.models import Citas, DetalleCitas
from apps.Catalogos.Pacientes.models import Pacientes
from apps.Modulo_Examen.Examen.models import Examen
from apps.Modulo_Medicamento.Medicamento.models import Medicamento
from apps.Catalogos.Medicos.models import Medicos


# Serializador para los detalles de las citas
class DetalleCitasSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleCitas
        fields = ['Diagnostico', 'Tratamiento']  # Solo estos campos para los detalles

# Serializador para los datos completos de una cita
class CitasWithDetailsSerializer(serializers.ModelSerializer):
    paciente = serializers.SerializerMethodField()  # Mostrar detalles del paciente
    examen = serializers.SerializerMethodField()    # Mostrar detalles del examen
    medicamento = serializers.SerializerMethodField()  # Mostrar detalles del medicamento
    medicos = serializers.SerializerMethodField()   # Mostrar detalles del médico
    DetalleCitas = DetalleCitasSerializer(many=True, read_only=True)  # Mostrar detalles relacionados

    class Meta:
        model = Citas
        fields = ['Num_citas', 'Fecha', 'Razon', 'Estado', 'Costo', 'paciente', 'examen', 'medicamento', 'medicos', 'DetalleCitas']

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

    def get_examen(self, obj):
        examen = obj.examen
        return {
            "NumExamen": examen.NumExamen,
            "FecExamen": examen.FecExamen,
            "Resultado": examen.Resultado,
            "Descripcion": examen.Descripcion,
        }

    def get_medicamento(self, obj):
        medicamento = obj.medicamento
        return {
            "Nombre": medicamento.Nombre,
            "Descripcion": medicamento.Descripcion,
            "NombreGenerico": medicamento.NombreGenerico,
            "Presentacion": medicamento.Presentacion,
            "Contradicciones": medicamento.Contradicciones,
            "EfectosSecundarios": medicamento.EfectosSecundarios,
        }

    def get_medicos(self, obj):
        medico = obj.medicos
        return {
            "Codigo": medico.Codigo,
            "Nombres": medico.Nombres,
            "Apellidos": medico.Apellidos,
            "FecNacimiento": medico.FecNacimiento,
            "Direccion": medico.Direccion,
            "Especialidad": medico.Especialidad,
            "Telefono": medico.Telefono,
        }

# Serializador para la creación de citas (acepta solo IDs y detalles)
class CitasCreateSerializer(serializers.ModelSerializer):
    paciente = serializers.IntegerField(write_only=True)  # Solo ID del paciente
    examen = serializers.IntegerField(write_only=True)    # Solo ID del examen
    medicamento = serializers.IntegerField(write_only=True)  # Solo ID del medicamento
    medicos = serializers.IntegerField(write_only=True)   # Solo ID del médico
    DetalleCitas = DetalleCitasSerializer(many=True, write_only=True)  # Detalles como objetos anidados

    class Meta:
        model = Citas
        fields = ['Num_citas', 'Fecha', 'Razon', 'Estado', 'Costo', 'paciente', 'examen', 'medicamento', 'medicos', 'DetalleCitas']
