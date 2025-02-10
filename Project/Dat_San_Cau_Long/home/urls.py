from django.urls import path
from . import views

urlpatterns = [
    # Đăng ký & Đăng nhập
    path("register/", views.register_view, name="register"),  
    path('customer-login/', views.customer_login, name='customer_login'),
    
    # URL trang chủ
    path('', views.home, name="home"),

    # URL Payment
    path('Payments/', views.Payments, name='Payments'),
    path('Payments/edit/<int:id>/', views.edit_Payment, name='edit_Payment'),
    path('Payments/new/', views.PaymentNew, name='Payment-new'),

    # URL Court
    path('Courts/', views.Courts, name='Courts'),  
    path('Court-edit/', views.edit_Court, name='Court-edit'),
    path('Court-new/', views.CourtNew, name='Court-new'), 
