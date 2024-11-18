from django.urls import path
from .views import MedicosApiView, MedicosDetails
urlpatterns = [
    path('', MedicosApiView.as_view()),
    path('<int:pk>', MedicosDetails.as_view()),
]