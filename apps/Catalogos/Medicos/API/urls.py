from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.Catalogos.Medicos.API.views import MedicosApiView



router = DefaultRouter()
router.register('', MedicosApiView, basename='medicos')

urlpatterns = [
    path('', MedicosApiView.as_view()),
]