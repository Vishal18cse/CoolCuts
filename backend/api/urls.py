from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import AppointmentListView, AppointmentDetailView, ServiceViewSet , AppointmentHistoryView

# this is automatic way of url routing 
router = DefaultRouter()
router.register(r'services', ServiceViewSet)
from .views import contact_form


urlpatterns = [
    path('appointments/', AppointmentListView.as_view(), name='appointment-list'),
    path('appointments/<int:pk>/', AppointmentDetailView.as_view(), name='appointment-detail'),
    path('user/appointments/', AppointmentHistoryView.as_view(), name='appointment-history'),
     path('contact/', contact_form, name='contact_form'),

    path('', include(router.urls)),
]
