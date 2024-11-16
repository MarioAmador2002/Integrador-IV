from django.urls import path, include

urlpatterns = [
    path('Citas/', include('apps.Modulo_Citas.Citas.API.urls')),
]