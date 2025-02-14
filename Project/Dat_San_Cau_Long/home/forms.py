from django import forms
from .models import Court, Payment, Booking

# Form cho việc tạo mới Payment
class PaymentNewForm(forms.Form):
    payment_id = forms.CharField(label="Payment ID", max_length=100)
    booking = forms.IntegerField(label="Booking ID", initial=2021)
    customer = forms.DateField(label="Customer")
    payment_date = forms.DateField(label="Payment Date")
    active = forms.BooleanField(label="Active", initial=True)

# Form cho việc tạo mới Court
class CourtNewForm(forms.Form):
    name_court = forms.CharField(label="Court Name", max_length=100)
    location = forms.CharField(label="Location", max_length=100)
    start_time = forms.TimeField(label="Start Time")
    end_time = forms.TimeField(label="End Time")
    status = forms.CharField(label="Status", max_length=50)
    type_court = forms.CharField(label="Court Type", max_length=50)
    cost_court = forms.DecimalField(label="Cost per Hour", max_digits=10, decimal_places=2)

class BookingNewForm(forms.Form):
    booking_id = forms.CharField(label="booking_id", max_length=100)
    start_time = forms.IntegerField(label="start_time", initial=2021)
    end_time = forms.DateField(label="end_time")
    booking_date = forms.DateField(label="booking_date")
    active = forms.BooleanField(label="active", initial=True)