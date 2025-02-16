from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from D_San_Mng.models import Court, Payment, Booking
from .forms import CourtNewForm, CourtEditForm, PaymentNewForm, BookingNewForm
import random
from .models import Payment
# Home view
def home(request):
    return render(request, 'home/index.html')

# Đăng ký tài khoản
def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("password2")
        if password != confirm_password:
            messages.error(request, "Mật khẩu không khớp!")
            return render(request, "home/register.html")
        if User.objects.filter(username=username).exists():
            messages.error(request, "Tên đăng nhập đã tồn tại!")
            return render(request, "home/register.html")
        user = User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, "Đăng ký thành công! Vui lòng đăng nhập.")
        return redirect("customer_login")  # Chuyển về trang đăng nhập
    return render(request, "home/register.html")


# Đăng nhập khách hàng
def customer_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")


        # tai khoan co dinh
        if username == "abc" and password == "123456":
            user, created = User.objects.get_or_create(username="abc", defaults={"is_active": True})
            login(request, user)
            messages.success(request, "Đăng nhập thành công với tài khoản cố định!")
            return redirect("home")


        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Đăng nhập thành công!")
            next_url = request.GET.get("next", "home")  # Chuyển hướng đến trang trước đó
            return redirect(next_url)
        else:
            messages.error(request, "Tên đăng nhập hoặc mật khẩu không đúng!")
    return render(request, "home/customer-login.html")


# List all Payments
def Payments(request):
    payments = Payment.objects.all()
    return render(request, 'home/Payments.html', {'payments': payments})


# Edit a Payment
def edit_Payment(request, id):
    payment = get_object_or_404(Payment, id=id)

    if request.method == "POST":
        payment_method = request.POST.get("payment_method")

        if payment_method == "cash":
            success = random.random() > 0.5  # 50% tỷ lệ thanh toán thành công
            payment.status = "Thành công" if success else "Thất bại"
        else:
            success = random.random() > 0.2  # 80% tỷ lệ thành công
            payment.status = "Đang xử lý" if success else "Thất bại"

        payment.save()

        if payment.status == "Thành công":
            return JsonResponse({"status": "success", "message": "Thanh toán thành công!"})
        elif payment.status == "Đang xử lý":
            return JsonResponse({"status": "pending", "message": "Đang xử lý thanh toán..."})
        else:
            return JsonResponse({"status": "failed", "message": "Thanh toán thất bại!"})

    return render(request, 'home/Payment-edit.html', {'payment': payment})




# Create a New Payment
def PaymentNew(request):
    if request.method == "POST":
        form = PaymentNewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanh toán mới đã được tạo thành công.")
            return redirect("Payments")
    else:
        form = PaymentNewForm()
    return render(request, 'home/Payment-new.html', {'form': form})


# List all Courts
def Court_KH(request, id=None): 
    courts = Court.objects.all()  # Fixed variable naming
    template = loader.get_template('home/Court-KH.html')
    context = {
        'courts': courts,  # Updated context key
    }
    return HttpResponse(template.render(context, request))

def Courts(request):
    courts = Court.objects.all()  # Fixed variable naming
    template = loader.get_template('home/Courts.html')
    context = {
        'courts': courts,  # Updated context key
    }
    return HttpResponse(template.render(context, request))

#  Edit Court
def edit_Court(request, id):  
    court = get_object_or_404(Court, id_court=id)  # Lấy sân cần chỉnh sửa

    if request.method == "POST":
        form = CourtEditForm(request.POST, court=court)
        if form.is_valid():
            court.name_court = form.cleaned_data['name_court']
            court.location = form.cleaned_data['location']
            court.start_time = form.cleaned_data['start_time']
            court.end_time = form.cleaned_data['end_time']
            court.status = form.cleaned_data['status']
            court.type_court = form.cleaned_data['type_court']
            court.cost_court = form.cleaned_data['cost_court']
            court.save()
            return redirect('Courts')  # Chuyển về danh sách sân
    else:
        form = CourtEditForm(court=court)  # Đổ dữ liệu cũ vào form

    return render(request, 'home/Court-edit.html', {'form': form, 'court': court})


# Thêm sân cầu lông mới
def CourtNew(request):
    if request.method == "POST":
        form = CourtNewForm(request.POST)
        print("Dữ liệu POST:", request.POST)  # Debug dữ liệu nhận được

        if form.is_valid():
            # Lưu thủ công vào database vì Form không có .save()
            Court.objects.create(
                name_court=form.cleaned_data["name_court"],
                location=form.cleaned_data["location"],
                start_time=form.cleaned_data["start_time"],
                end_time=form.cleaned_data["end_time"],
                status=form.cleaned_data["status"],
                type_court=form.cleaned_data["type_court"],
                cost_court=form.cleaned_data["cost_court"]
            )
            
            messages.success(request, "Sân cầu lông đã được thêm thành công!")
            print("Saved successfully!")  # Debug xem đã lưu chưa
            return redirect("Courts")  # Chuyển hướng về danh sách sân
        else:
            print("Lỗi form:", form.errors)  # Debug lỗi form
            messages.error(request, "Có lỗi xảy ra. Vui lòng kiểm tra lại thông tin.")
    
    else:
        form = CourtNewForm()  # Khởi tạo form khi vào trang

    return render(request, 'home/Court-new.html', {'form': form})

def delete_court(request, court_id):
    print(f"Nhận yêu cầu xóa sân ID: {court_id}")  # Debug
    if request.method == "POST":  # Đổi từ DELETE thành POST
        try:
            court = get_object_or_404(Court, id_court=court_id)  # Sửa id → id_court
            court.delete()
            print(f"Đã xóa sân {court_id}")  # Debug
            return JsonResponse({"success": True})
        except Exception as e:
            print(f"Lỗi khi xóa sân: {e}")  # Debug
            return JsonResponse({"success": False, "error": str(e)}, status=500)
    return JsonResponse({"success": False, "error": "Invalid request"}, status=400)


# List all Payments
def Bookings(request):
    Bookings = Booking.objects.all()  # Fixed variable naming
    template = loader.get_template('home/Bookings.html')
    context = {
        'Bookings': Bookings,  # Updated context key
    }
    return HttpResponse(template.render(context, request))


# Edit a Payment
def edit_Bookings(request, booking_id):  # Sử dụng 'booking_id' thay vì 'id'
    # Tìm bản ghi Booking dựa trên booking_id
    booking = get_object_or_404(Booking, booking_id=booking_id)
    return render(request, 'edit_booking.html', {'booking': booking})

def process_payment(request):
    return HttpResponse("Processing payment...")

def submit_booking(request):
    if request.method == "POST":
        form = BookingNewForm(request.POST)
        if form.is_valid():
            booking = form.save()
            return HttpResponseRedirect("/Bookings")  # Điều hướng sau khi đặt sân thành công
    else:
        form = BookingNewForm()

    return render(request, "home/Booking/submit-booking.html", {"form": form})
# Create a New Payment
def BookingNew(request):
    if request.method == "POST":
        form = BookingNewForm(request.POST)
        if form.is_valid():
            # Create and save the Payment instance
            Booking = Booking(
                booking_id=form.cleaned_data['booking_id'],
                start_time=form.cleaned_data['start_time'],
                end_time=form.cleaned_data['end_time'],
                booking_date=form.cleaned_data['booking_date'],
                active=form.cleaned_data['active'],
            )
            Booking.save()
            return HttpResponseRedirect("/Bookings")
    else:
        form = BookingNewForm()

    template = loader.get_template('home/Booking/Booking-new.html')  # Check this path
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))
