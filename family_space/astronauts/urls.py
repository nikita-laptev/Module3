from django.urls import path
from .views import GagarinFlightView

urlpatterns = [
    path('api/gagarin-flight', GagarinFlightView.as_view(), name='gagarin_flight'),
]
