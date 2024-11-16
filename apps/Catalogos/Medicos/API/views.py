from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.Catalogos.Medicos.models import Medicos
from apps.Catalogos.Medicos.API.serializers import MedicosSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated

class MedicosApiView(APIView):
    """
    Vista para listar todos los Medicos, actualizar agregar y eliminar
    """

    @swagger_auto_schema(responses={200: MedicosSerializer(many=True)})
    def get(self, request):
        """
        Listar todos los Medico.
        """
        medicos = Medicos.objects.all()
        serializer = MedicosSerializer(Medicos, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=MedicosSerializer, responses={201: MedicosSerializer})
    def post(self, request):
        """
        agregar un nuevo medico
        """
        serializer = MedicosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=MedicosSerializer, responses={200: MedicosSerializer})
    def patch(self, request, pk):
        """
        Actualizar parcialmente un medico existente
        """
        try:
            medicos = Medicos.objects.get(pk=pk)
        except Medicos.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = MedicosSerializer(Medicos, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        """
        Eliminar un paciente por su ID.
        """
        try:
            medicos = Medicos.objects.get(pk=pk)
        except Medicos.DoesNotExist:
            return Response({'error': 'medicos no encontrados'}, status=status.HTTP_404_NOT_FOUND)
        Medicos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
