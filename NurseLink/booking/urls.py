from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('booking/', views.booking, name='booking'),
    path('patient-booking/', views.patient_booking, name='patient_booking'),
    path('booking-success/', views.booking_success, name='booking_success'),
]