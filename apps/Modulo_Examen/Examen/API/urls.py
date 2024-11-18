from django.urls import path
from .views import ExamenListAPIView, ExamenDetailAPIView, ExamenCreateAPIView

app_name = "Citas"
urlpatterns = [
    path('examen/', ExamenListAPIView.as_view(), name='examen-list'),  # GET todos los examen
    path('examen/<int:pk>/', ExamenDetailAPIView.as_view(), name='examen-detail'),  # GET por ID
    path('examen/create/', ExamenCreateAPIView.as_view(), name='examen-create'),  # POST nueva cita

]