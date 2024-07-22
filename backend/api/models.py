from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Appointment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('done', 'Done'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100, null=True, blank=True)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    booking_time = models.DateTimeField(default=timezone.now) 
    checklist = models.JSONField(default=list, blank=True)  # Use JSONField to store checklist as JSON
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')  # Add status field


    def __str__(self):
        return f"{self.customer_name} - {self.appointment_date} at {self.appointment_time}"

class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    
    def __str__(self):
        return self.name


class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} regarding {self.subject}"
