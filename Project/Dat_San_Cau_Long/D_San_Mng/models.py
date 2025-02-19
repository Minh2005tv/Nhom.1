from django.db import models

# Customer model
class Customer(models.Model):
    name = models.CharField(max_length=255)
    customer_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.customer_id} {self.name}"

# Booking model
class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    booking_date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='bookings')

    def __str__(self):
        return f"Booking {self.booking_id} for Customer {self.customer.name}"
    
    # Payment model
class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='payments')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='payments')
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Failed', 'Failed'),
    ])
    method = models.CharField(max_length=50, choices=[
        ('Credit Card', 'Credit Card'),
        ('Debit Card', 'Debit Card'),
        ('Cash', 'Cash'),
        ('Online', 'Online'),
    ])
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Payment {self.payment_id} - {self.status}"
    
   # Court model
class Court(models.Model):
    id_court = models.AutoField(primary_key=True)
    name_court = models.CharField(max_length=255)
    cost_court = models.DecimalField(max_digits=10, decimal_places=2)
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=255)
    type_court = models.CharField(max_length=255, choices=[
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
    ])
    status = models.CharField(max_length=50, choices=[
        ('Closed', 'Closed'),
        ('Maintenance', 'Maintenance'),
        ('Available', 'Available'),
    ])
    
    # Loại lịch đặt sân
    schedule_type = models.CharField(
        max_length=50,
        choices=[
            ('Fixed', 'Lịch cố định'),  # Đặt theo giờ + thứ cố định trong tuần, tối thiểu 1 tháng
            ('Single', 'Lịch ngày'),  # Đặt cho 1 lần chơi
            ('Flexible', 'Lịch linh hoạt')  # Tổng số giờ chơi trong 1 tháng, tự tìm giờ trống
        ],
        default='Single'  # Giá trị mặc định để tránh lỗi migration
    )
    min_duration_months = models.IntegerField(default=1, help_text="Chỉ áp dụng cho lịch cố định")
    total_hours_per_month = models.IntegerField(null=True, blank=True, help_text="Chỉ áp dụng cho lịch linh hoạt")

    def __str__(self):
        return f"Court {self.id_court} - {self.name_court} ({self.status})"