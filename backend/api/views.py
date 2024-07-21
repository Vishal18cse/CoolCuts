from rest_framework import generics
from .models import Appointment ,Service
from .serializers import AppointmentSerializer , ServiceSerializer
from rest_framework.exceptions import ValidationError
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response


class AppointmentListView(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def perform_create(self, serializer):
        appointment_date = serializer.validated_data['appointment_date']
        appointment_time = serializer.validated_data['appointment_time']

        if Appointment.objects.filter(appointment_date=appointment_date, appointment_time=appointment_time).exists():
            raise ValidationError('This time slot is already booked.')

        serializer.save()

class AppointmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def perform_update(self, serializer):
        appointment_date = serializer.validated_data.get('appointment_date', self.get_object().appointment_date)
        appointment_time = serializer.validated_data.get('appointment_time', self.get_object().appointment_time)

        if Appointment.objects.filter(appointment_date=appointment_date, appointment_time=appointment_time).exclude(pk=self.get_object().pk).exists():
            raise ValidationError('This time slot is already booked.')

        serializer.save()
class AppointmentHistoryView(APIView):

    def get(self, request):
        user_id = request.query_params.get('user_id')
        if not user_id:
            return Response({"error": "User ID is required"}, status=400)

        appointments = Appointment.objects.filter(user_id=user_id)
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer