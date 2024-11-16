from django.urls import path
from .views import CitasListAPIView, CitasDetailAPIView, CitasCreateAPIView

app_name = "Citas"
urlpatterns = [
    path('citas/', CitasListAPIView.as_view(), name='citas-list'),  # GET todas las citas
    path('citas/<int:pk>/', CitasDetailAPIView.as_view(), name='citas-detail'),  # GET por ID
    path('citas/create/', CitasCreateAPIView.as_view(), name='citas-create'),  # POST nueva cita

]
