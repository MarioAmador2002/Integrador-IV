from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.Catalogos.Medicos.models import Medicos
from apps.Catalogos.Medicos.API.serializers import MedicosSerializer
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from apps.Seguridad.permissions import CustomPermission
from config.Utils.Pagination import  PaginationMixin
import logging.handlers


# Configura el logger
logger = logging.getLogger(__name__)

class MedicosApiView(PaginationMixin, APIView):
    """
    Vista para Agregar, listar, actualizar y eliminar un medicos
    """
    permission_classes = [IsAuthenticated, CustomPermission]
    model = Medicos

    @swagger_auto_schema(responses={200: MedicosSerializer(many=True)})
    def get(self, request):
        """
        Listar todos los Medicos.
        """
        logger.info("GET request to list all medicos")
        medicos = Medicos.objects.all().order_by('id')
        page = self.paginate_queryset(medicos, request)

        if page is not None:
            serializer = MedicosSerializer(page, many=True)
            logger.info("Paginated response for Medicos")
            return self.get_paginated_response(serializer.data)

        serializer = MedicosSerializer(medicos, many=True)
        logger.error("Returning all Medicos without pagination")
        return Response(serializer.data)


    @swagger_auto_schema(request_body=MedicosSerializer, responses={201: MedicosSerializer})
    def post(self, request):
        """
        Metodo para agregar un nuevo registro de Medicos
        """
        logger.info("POST request to create a new Medicos")

        serializer = MedicosSerializer(data=request.data)
        # Validar si el Medico ya existe solo por el Codigo
        codigo = request.data.get('Codigo')

        if Medicos.objects.filter(Codigo=codigo).exists():
            logger.warning("El medico ya existe con el Codigo: %s", codigo)
            return Response({"detail": "El Medico ya existe."}, status=status.HTTP_400_BAD_REQUEST)


        if serializer.is_valid():
            serializer.save()
            logger.info("Medico created successfully")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error("Failed to create Medico: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MedicosDetails(APIView):
    """
    Vista para obtener, actualizar o eliminar un Medico específico.
    """
    permission_classes = [IsAuthenticated, CustomPermission]
    model = Medicos
    @swagger_auto_schema(request_body=MedicosSerializer, responses={200: MedicosSerializer(many=True)})
    def put(self, request, pk):
        """
        Actualizar completamente un Medico por su ID.
        """

        logger.info("PUT request to update paciente with ID: %s", pk)
        medicos = get_object_or_404(Medicos, id=pk)
        if not Medicos:
            return Response({'error': 'Medico no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, medicos)
        serializer = MedicosSerializer(medicos, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Medico updated successfully with ID: %s", pk)
            return Response(serializer.data)

            logger.error("Failed to update Medico with ID: %s. Errors: %s", pk, serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        @swagger_auto_schema(request_body=MedicosSerializer, responses={200: MedicosSerializer(many=True)})
        def patch(self, request, pk):
            """
            Actualizar parcialmente un Medico por su ID.
            """
            logger.info("PATCH request to partially update Medico with ID: %s", pk)
            medicos = get_object_or_404(Medicos, id=pk)
            if not medicos:
                return Response({'error': 'paciente no encontrado'}, status=status.HTTP_404_NOT_FOUND)

            self.check_object_permissions(request, medicos)  # Verificación de permisos
            serializer = MedicosSerializer(medicos, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                logger.info("Medico partially updated successfully with ID: %s", pk)
                return Response(serializer.data)

            logger.error("Failed to partially update Medico with ID: %s. Errors: %s", pk, serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        @swagger_auto_schema(responses={204: 'No Content'})
        def delete(self, request, pk):
            """
            Eliminar un medico por su ID.
            """
            logger.info("DELETE request to delete Medico with ID: %s", pk)
            medicos = get_object_or_404(Medicos, id=pk)
            if not medicos:
                return Response({'error': 'Medicos no encontrado'}, status=status.HTTP_404_NOT_FOUND)

            self.check_object_permissions(request, medicos)  # Verificación de permisos
            medicos.delete()
            logger.info("medicos deleted successfully with ID: %s", pk)
            return Response(status=status.HTTP_204_NO_CONTENT)

