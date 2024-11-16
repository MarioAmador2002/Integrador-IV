from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.Catalogos.Pacientes.models import Pacientes
from apps.Catalogos.Pacientes.API.serializers import PacientesSerializer
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from apps.Seguridad.permissions import CustomPermission
from config.Utils.Pagination import  PaginationMixin
import logging.handlers


# Configura el logger
logger = logging.getLogger(__name__)

class PacientesApiView(APIView):
    """
    Vista para agregar, listar, actualizar y eliminar un paciente
    """
    permission_classes = [IsAuthenticated, CustomPermission]
    model = Pacientes

    @swagger_auto_schema(responses={200: PacientesSerializer(many=True)})
    def get(self, request):
        """
        Listar todas los pacientes.
        """
        logger.info("GET request to list all pacientes")
        paciente = Pacientes.objects.all().order_by('id')
        page = self.paginate_queryset(paciente, request)

        if page is not None:
            serializer = PacientesSerializer(page, many=True)
            logger.info("Paginated response for pacientes")
            return self.get_paginated_response(serializer.data)

        serializer = PacientesSerializer(paciente, many=True)
        logger.error("Returning all pacientes without pagination")
        return Response(serializer.data)


    @swagger_auto_schema(request_body=PacientesSerializer, responses={201: PacientesSerializer})
    def post(self, request):
        """
        agregar un nuevo paciente
        """
        logger.info("POST request to create a new paciente")

        serializer = PacientesSerializer(data=request.data)
        # Validar si el paciente ya existe solo por el Codigo
        codigo = request.data.get('Codigo')

        if Pacientes.objects.filter(Codigo=codigo).exists():
            logger.warning("El paciente ya existe con el Codigo: %s", codigo)
            return Response({"detail": "El paciente ya existe."}, status=status.HTTP_400_BAD_REQUEST)


        if serializer.is_valid():
            serializer.save()
            logger.info("paciente created successfully")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error("Failed to create paciente: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PacienteDetails(APIView):
    """
    Vista para obtener, actualizar o eliminar un paciente específico.
    """


    permission_classes = [IsAuthenticated, CustomPermission]
    model = Pacientes
    @swagger_auto_schema(request_body=PacientesSerializer, responses={200: PacientesSerializer(many=True)})
    def put(self, request, pk):
        """
        Actualizar completamente un paciente por su ID.
        """

        logger.info("PUT request to update paciente with ID: %s", pk)
        paciente = get_object_or_404(Pacientes, id=pk)
        if not paciente:
            return Response({'error': 'paciente no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, paciente)
        serializer = PacientesSerializer(paciente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("paciente updated successfully with ID: %s", pk)
            return Response(serializer.data)

            logger.error("Failed to update paciente with ID: %s. Errors: %s", pk, serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        @swagger_auto_schema(request_body=PacientesSerializer, responses={200: PacientesSerializer(many=True)})
        def patch(self, request, pk):
            """
            Actualizar parcialmente un paciente por su ID.
            """
            logger.info("PATCH request to partially update paciente with ID: %s", pk)
            departamento = get_object_or_404(Pacientes, id=pk)
            if not paciente:
                return Response({'error': 'paciente no encontrado'}, status=status.HTTP_404_NOT_FOUND)

            self.check_object_permissions(request, paciente)  # Verificación de permisos
            serializer = PacientesSerializer(paciente, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                logger.info("paciente partially updated successfully with ID: %s", pk)
                return Response(serializer.data)

            logger.error("Failed to partially update paciente with ID: %s. Errors: %s", pk, serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        @swagger_auto_schema(responses={204: 'No Content'})
        def delete(self, request, pk):
            """
            Eliminar un paciente por su ID.
            """
            logger.info("DELETE request to delete paciente with ID: %s", pk)
            paciente = get_object_or_404(Pacientes, id=pk)
            if not paciente:
                return Response({'error': 'paciente no encontrado'}, status=status.HTTP_404_NOT_FOUND)

            self.check_object_permissions(request, paciente)  # Verificación de permisos
            paciente.delete()
            logger.info("paciente deleted successfully with ID: %s", pk)
            return Response(status=status.HTTP_204_NO_CONTENT)


