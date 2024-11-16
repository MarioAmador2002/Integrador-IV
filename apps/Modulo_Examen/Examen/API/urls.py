from django.urls import path
from .views import ExamenAPI

app_name = "Citas"
urlpatterns = [
    path('', ExamenAPI.as_view(), name='examen'),
]