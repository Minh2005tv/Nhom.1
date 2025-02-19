from django.contrib import admin
from .models import Customer, Booking, Payment, Court

#admin.site.register(Customer)
#admin.site.register(Booking)
#admin.site.register(Payment)
#admin.site.register(Court)


class CustomerAdmin(admin.ModelAdmin):
  list_display = ("name", "email", "phone",)

class CourtAdmin(admin.ModelAdmin):
    list_display = ("id_court", "name_court", "cost_court", "start_time", "end_time", "schedule_type", "status")
    list_filter = ("schedule_type", "status", "type_court")
    search_fields = ("name_court", "location")

class BookingAdmin(admin.ModelAdmin):
  list_display = ("start_time", "end_time", "booking_date",)

class PaymentAdmin(admin.ModelAdmin):
  list_display = ("payment_id", "customer", "payment_date",)
 
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Court, CourtAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Payment, PaymentAdmin)