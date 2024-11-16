from django.urls import path, include
urlpatterns = [
    path('Pacientes/', include('apps.Catalogos.Pacientes.API.urls')),
    path('Medicos/', include('apps.Catalogos.Medicos.API.urls')),
]