from django.db import transaction
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.Catalogos.Medicos.models import Medicos
from apps.Catalogos.Pacientes.models import Pacientes
from apps.Modulo_Examen.Examen.models import Examen, DetalleExamen
from apps.Modulo_Examen.Examen.API.serializers import ExamenWithDetailsSerializer, ExamenCreateSerializer
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from apps.Seguridad.permissions import CustomPermission
from config.Utils.Pagination import  PaginationMixin
import logging.handlers


# Configura el logger
logger = logging.getLogger(__name__)


class ExamenListAPIView(PaginationMixin, APIView):
    """
         Vista para listar todos los Examenes y crear uno nuevo
    """

    permission_classes = [IsAuthenticated, CustomPermission]
    model = Examen

    @swagger_auto_schema(responses={200: ExamenWithDetailsSerializer(many=True)})
    def get(self, request):

        """
                Obtener una lista de todos los Examenes registrados
        """
        logger.info("GET request to list all Examen")
        examen = Examen.objects.all().order_by('id')
        page = self.paginate_queryset(examen, request)

        if not examen:
            return Response({"detail": "No se encontraron Examenes."}, status=status.HTTP_400_BAD_REQUEST)

        if page is not None:
            serializer = ExamenWithDetailsSerializer(page, many=True)
            logger.info("Paginated response for Examen")
            return self.get_paginated_response(serializer.data)

        serializer = ExamenWithDetailsSerializer(examen, many=True)
        logger.error("Returning all Examen without pagination")
        return Response(serializer.data)

        examen = Examen.objects.all().order_by('id')
        serializer = ExamenWithDetailsSerializer(examen, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ExamenDetailAPIView(APIView):
        """
           Endpoint para obtener un Examen específico por ID con sus detalles relacionados.
           """

        @swagger_auto_schema(responses={200: ExamenWithDetailsSerializer})
        def get(self, request, pk):
            examen = get_object_or_404(Examen, pk=pk)
            serializer = ExamenWithDetailsSerializer(examen)
            return Response(serializer.data, status=status.HTTP_200_OK)


class ExamenCreateAPIView(APIView):
    """
       Endpoint para crear un nuevo Examen con sus detalles relacionados.
       """

    @swagger_auto_schema(request_body=ExamenCreateSerializer, responses={201: ExamenWithDetailsSerializer})
    def post(self, request):

        data = request.data
        try:
            with transaction.atomic():
                # Validar si el examen ya existe solo por el NumExamen
                NumExamen = data.get('NumExamen')
                if Examen.objects.filter(NumExamen=NumExamen).exists():
                    logger.warning("El examen ya existe con el NumExamen: %s", NumExamen)
                    return Response({"detail": "El examen ya existe."}, status=status.HTTP_400_BAD_REQUEST)

                    # Validar las relaciones
                paciente_id = data.get('Paciente')
                medico_id = data.get('Medicos')

                paciente = get_object_or_404(Pacientes, id=paciente_id)
                medico = get_object_or_404(Medicos, id=medico_id)

                # Crear la cita
                examen = Examen.objects.create(
                    NumExamen=NumExamen,
                    FecExamen=data.get('FecExamen'),
                    Resultado=data.get('Resultado'),
                    Descripcion=data.get('Descripcion'),
                    paciente=paciente,
                    medicos=medico
                )
                # Crear los detalles del examen
                detalles = data.get('DetallesExamen', [])
                for detalle in detalles:

                    DetalleExamen.objects.create(
                        TipoExamen=detalle.get('TipoExamen'),
                        Estado=detalle.get('Estado'),
                        Costo = detalle.get('Costo'),
                        Observacion = detalle.get('Observacion'),
                        examen= Examen,
                    )

                    # Serializar y devolver la cita creada
                    serializer = ExamenWithDetailsSerializer(examen)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            logger.error("Error al crear la examen: %s", str(e))
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)













