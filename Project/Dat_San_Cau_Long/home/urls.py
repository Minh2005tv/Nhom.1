#urls.py
from django.urls import path
from . import views

urlpatterns = [
    # URL trang chủ
    path('', views.home, name="home"),

    # URL Payment
    path('Payments/', views.Payments, name='Payments'),  # Thêm dấu gạch chéo ở cuối
    path('Payments/edit/<int:id>/', views.edit_Payment, name='edit_Payment'),
    path('Payments/new/', views.PaymentNew, name='Payment-new'),

    # URL Court
    path('Courts/', views.Courts, name='Courts'),  # Sửa lại đúng view cho danh sách sân
    path('Court-edit/', views.edit_Court, name='Court-edit'),
    path('Courts/new/', views.CourtNew, name='Court-new'),  # Sửa lại view cho thêm mới sân
]
