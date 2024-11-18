from django.db import transaction
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.Modulo_Citas.Citas.models import Citas, DetalleCitas
from apps.Catalogos.Pacientes.models import Pacientes
from apps.Modulo_Examen.Examen.models import Examen
from apps.Modulo_Medicamento.Medicamento.models import Medicamento
from apps.Catalogos.Medicos.models import Medicos
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from apps.Seguridad.permissions import CustomPermission
from config.Utils.Pagination import  PaginationMixin
import logging.handlers
from apps.Modulo_Citas.Citas.API.serializers import CitasWithDetailsSerializer, CitasCreateSerializer



# Configura el logger
logger = logging.getLogger(__name__)


class CitasListAPIView(PaginationMixin, APIView):
    """
      Vista para listar todas las citas y crear una nueva
      """
    permission_classes = [IsAuthenticated, CustomPermission]
    model = Citas


    @swagger_auto_schema(responses={200: CitasWithDetailsSerializer(many=True)})
    def get(self, request):
        """
           Obtener una lista de todas las citas registradas
        """
        logger.info("GET request to list all Citas")
        citas = Citas.objects.all().order_by('id')
        page = self.paginate_queryset(citas, request)

        if not citas:
            return Response({"detail": "No se encontraron citas."}, status=status.HTTP_400_BAD_REQUEST)

        if page is not None:
            serializer = CitasWithDetailsSerializer(page, many=True)
            logger.info("Paginated response for Citas")
            return self.get_paginated_response(serializer.data)

        serializer = CitasWithDetailsSerializer(citas, many=True)
        logger.error("Returning all Citas without pagination")
        return Response(serializer.data)

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
                # Validar si la cita ya existe solo por el Num_citas
                Num_citas = data.get('Num_citas')
                if Citas.objects.filter(Num_citas=Num_citas).exists():
                    logger.warning("La cita ya existe con el Num_citas: %s", Num_citas)
                    return Response({"detail": "La cita ya existe."}, status=status.HTTP_400_BAD_REQUEST)

                # Validar las relaciones
                paciente_id = data.get('Paciente')
                examen_id = data.get('Examen')
                medicamento_id = data.get('Medicamento')
                medico_id = data.get('Medicos')

                paciente = get_object_or_404(Pacientes, id=paciente_id)
                examen = get_object_or_404(Examen, id=examen_id)
                medicamento = get_object_or_404(Medicamento, id=medicamento_id)
                medico = get_object_or_404(Medicos, id=medico_id)

                # Crear la cita
                cita = Citas.objects.create(
                    Num_citas=Num_citas,
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
            logger.error("Error al crear la cita: %s", str(e))
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

