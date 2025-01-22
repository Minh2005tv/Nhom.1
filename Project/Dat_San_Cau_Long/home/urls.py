#urls.py
from django.urls import path
from . import views

urlpatterns = [
    # URL trang chủ
    path('', views.home, name="home"),

    # URL Payment
    path('Payments/', views.Payments, name='Payments'),
    path('Payments/edit/<int:id>/', views.edit_Payment, name='edit_Payment'),
    path('Payments/new/', views.PaymentNew, name='Payment-new'),

    # URL Court
    path('Courts/', views.Courts, name='Courts'),
    path('Courts/edit/<int:id>/', views.edit_Court, name='edit_Court'),
    path('Courts/new/', views.CourtNew, name='Court-new'),
]