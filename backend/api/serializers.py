from rest_framework import serializers
from .models import Appointment , Service
from datetime import datetime 



class AppointmentSerializer(serializers.ModelSerializer):
    checklist = serializers.JSONField(required=False)
    appointment_time = serializers.CharField() 

    class Meta:
        model = Appointment
        fields = ['id', 'customer_name', 'appointment_date', 'appointment_time', 'checklist']
    
    def validate_appointment_time(self, value):
        try:
            # Convert 12-hour format with AM/PM to 24-hour format
            time_obj = datetime.strptime(value, '%I:%M %p').time()
        except ValueError:
            raise serializers.ValidationError("Time has wrong format. Use 'HH:MM AM/PM'.")
        return time_obj

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'price']