from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from .serializers import ExamenSerializer
from apps.Modulo_Examen.Examen.models import Examen, DetalleExamen
from apps.Catalogos.Pacientes.models import Pacientes
from apps.Catalogos.Medicos.models import Medicos
from drf_yasg.utils import swagger_auto_schema

class ExamenAPI(APIView):
    @swagger_auto_schema(request_body=ExamenSerializer)
    def post(self, request):
        serializer = ExamenSerializer(data=request.data)

        if serializer.is_valid():
            try:
                with transaction.atomic():
                    examen = Examen.objects.create(
                        paciente=get_object_or_404(Pacientes, pk=serializer.validated_data['paciente']),
                        medico=get_object_or_404(Medicos, pk=serializer.validated_data['medico']),
                        NumExamen=serializer.validated_data['NumExamen'],
                        FecExamen=serializer.validated_data['FecExamen'],
                        Resultado=serializer.validated_data['Resultado'],
                        Descripcion=serializer.validated_data['Descripcion'],
                    )
                    detalles = serializer.validated_data.get('detalles', [])
                    for detalle_data in detalles:
                        DetalleExamen.objects.create(
                            TipoExamen=detalle_data['TipoExamen'],
                            Estado=detalle_data['Estado'],
                            Observacion=detalle_data['Observacion'],
                            examen=examen,
                        )
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={200: ExamenSerializer(many=True)})
    def get(self, request):
        try:
            examenes = Examen.objects.all()
            serializer = ExamenSerializer(examenes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



