from django.urls import path
from . import views

urlpatterns = [
    path('customer/', views.Customer, name='customer'),
    path('booking/', views.Booking, name='booking'),
    path('payment/', views.Payment, name='payment'),
    path('court/', views.Court, name='court'),
]