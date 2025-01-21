from django.urls import path
from . import views

urlpatterns = [
    path('D_San_Mng/', views.Customer, name='D_San_Mng'),
    path('D_San_Mng/', views.Booking, name='D_San_Mng'),
    path('D_San_Mng/', views.Payment, name='D_San_Mng'),
    path('D_San_Mng/', views.Court, name='D_San_Mng'),
]