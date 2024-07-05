# from django import forms
# from .models import Appointment

# class AppointmentForm(forms.ModelForm):
#     class Meta:
#         model = Appointment
#         fields = ['customer_name', 'appointment_date', 'appointment_time', 'checklist']

#     checklist = forms.CharField(widget=forms.HiddenInput(), required=False)

from django import forms
from .models import Appointment
from django.utils import timezone
from datetime import datetime, timedelta

# TIME_CHOICES = [
#     (datetime.strftime((datetime.min + timedelta(hours=h)).time(), '%I:%M %p'), datetime.strftime((datetime.min + timedelta(hours=h)).time(), '%I:%M %p'))
#     for h in range(9, 21)
# ]
def generate_time_slots(start_time, end_time, slot_duration):
    time_slots = []
    current_time = start_time
    while current_time < end_time:
        slot = current_time.strftime('%I:%M %p')
        time_slots.append((slot, slot))
        current_time += slot_duration
    return time_slots

# Generate time slots with a gap of 1 hour from 09:00 AM to 09:00 PM
start_time = datetime.strptime('09:00 AM', '%I:%M %p')
end_time = datetime.strptime('09:00 PM', '%I:%M %p')
slot_duration = timedelta(hours=1)
TIME_CHOICES = generate_time_slots(start_time, end_time, slot_duration)

class AppointmentForm(forms.ModelForm):
    appointment_time = forms.ChoiceField(choices=TIME_CHOICES, widget=forms.Select(), required=True)
    
    class Meta:
        model = Appointment
        fields = ['customer_name', 'appointment_date', 'appointment_time', 'checklist']
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date'}),
        }
        help_texts = {
            'appointment_time': 'Select a time slot.',
        }

    checklist = forms.CharField(widget=forms.HiddenInput(), required=False)

