from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db import transaction
from drf_yasg.utils import swagger_auto_schema
from apps.Modulo_Citas.Citas.models import Citas, DetalleCitas
from .serializers import CitasWithDetailsSerializer, CitasCreateSerializer, DetalleCitasSerializer
from apps.Catalogos.Pacientes.models import Pacientes
from apps.Modulo_Examen.Examen.models import Examen
from apps.Modulo_Medicamento.Medicamento.models import Medicamento
from apps.Catalogos.Medicos.models import Medicos

class CitasListAPIView(APIView):
    """
    Endpoint para obtener todas las citas con sus detalles relacionados.
    """
    @swagger_auto_schema(responses={200: CitasWithDetailsSerializer(many=True)})
    def get(self, request):
        citas = Citas.objects.all()
        serializer = CitasWithDetailsSerializer(citas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CitasDetailAPIView(APIView):
    """
    Endpoint para obtener una cita específica por ID con sus detalles relacionados.
    """
    @swagger_auto_schema(responses={200: CitasWithDetailsSerializer})
    def get(self, request, pk):
        cita = get_object_or_404(Citas, pk=pk)
        serializer = CitasWithDetailsSerializer(cita)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CitasCreateAPIView(APIView):
    """
    Endpoint para crear una nueva cita con sus detalles relacionados.
    """
    @swagger_auto_schema(request_body=CitasCreateSerializer, responses={201: CitasWithDetailsSerializer})
    def post(self, request):
        data = request.data
        try:
            with transaction.atomic():
                # Validar las relaciones
                paciente = get_object_or_404(Pacientes, id=data.get('paciente'))
                examen = get_object_or_404(Examen, id=data.get('examen'))
                medicamento = get_object_or_404(Medicamento, id=data.get('medicamento'))
                medico = get_object_or_404(Medicos, id=data.get('medicos'))

                # Crear la cita
                cita = Citas.objects.create(
                    Num_citas=data.get('Num_citas'),
                    Fecha=data.get('Fecha'),
                    Razon=data.get('Razon'),
                    Estado=data.get('Estado'),
                    Costo=data.get('Costo'),
                    paciente=paciente,
                    examen=examen,
                    medicamento=medicamento,
                    medicos=medico
                )

                # Crear los detalles de la cita
                detalles = data.get('DetalleCitas', [])
                for detalle in detalles:
                    DetalleCitas.objects.create(
                        Diagnostico=detalle.get('Diagnostico'),
                        Tratamiento=detalle.get('Tratamiento'),
                        citas=cita
                    )

                # Serializar y devolver la cita creada
                serializer = CitasWithDetailsSerializer(cita)
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
