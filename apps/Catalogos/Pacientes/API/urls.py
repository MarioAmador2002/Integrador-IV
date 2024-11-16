from django.urls import path
from .views import PacientesApiView, PacienteDetails
urlpatterns = [
    path('', PacientesApiView.as_view()),
    path('<int:pk>', PacienteDetails.as_view()),
]