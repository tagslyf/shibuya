from rest_framework import viewsets

from appointment.models import Appointment, Doctor, Patient
from appointment.serializers import AppointmentSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    model = Appointment
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
