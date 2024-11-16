from django.urls import path, include
urlpatterns = [
    path('Examen/', include('apps.Modulo_Examen.Examen.API.urls')),
]