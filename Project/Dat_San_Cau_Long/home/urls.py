from django.urls import path
from . import views
from .views import delete_court
from django.conf import settings
from django.conf.urls.static import static
from .views import delete_court

urlpatterns = [
    # Đăng ký & Đăng nhập
    path("register/", views.register_view, name="register"),  
    path('customer-login/', views.customer_login, name='customer_login'),

    # URL trang chủ
    path('', views.home, name="home"),

    # URL Payment
    path('Payments/', views.Payments, name='Payments'),
    
    

   

    # URL Court
    path('Courts/', views.Courts, name='Courts'), 
    path('Court-KH/', views.Court_KH, name='Court_KH'),
    path('Court-edit/<int:id>/', views.edit_Court, name='Court-edit'),
    path('Court-new/', views.CourtNew, name='Court-new'), 
    path('Court-delete/<int:court_id>/', delete_court, name="delete_court"),

    #URl Booking
    path('', views.home, name = "home"),
    path('Bookings/', views.Bookings, name='Bookings'),
    path('edit_Bookings/<int:id>/', views.edit_Bookings, name='edit_Bookings'),
    path('Booking-new', views.BookingNew, name='Booking-new'),
    path('submit-booking/', views.submit_booking, name='submit_booking'),
    path('payment/', views.process_payment, name='process_payment'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)