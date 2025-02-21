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
    courts = Court.objects.all()
    return render(request, 'home.html', {'courts': courts})

# Đăng ký tài khoản
def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("password2")
        if password != confirm_password:
            messages.error(request, "Mật khẩu không khớp!")
            return render(request, "home/Customer/register.html")
        if User.objects.filter(username=username).exists():
            messages.error(request, "Tên đăng nhập đã tồn tại!")
            return render(request, "home/Customer/register.html")
        user = User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, "Đăng ký thành công! Vui lòng đăng nhập.")
        return redirect("customer_login")  # Chuyển về trang đăng nhập
    return render(request, "home/Customer/register.html")


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
    return render(request, "home/Customer/customer-login.html")


# List all Payments
def Payments(request):
    payments = Payment.objects.all()
    return render(request, 'home/Payment/Payments.html', {'payments': payments})


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

    return render(request, 'home/Payment/Payment-edit.html', {'payment': payment})




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
    return render(request, 'home/Payment/Payment-new.html', {'form': form})


# List all Courts
def Court_KH(request, id=None):
    courts = Court.objects.all()
    template = loader.get_template('home/Court/Court-KH.html')
    context = {
        'courts': courts,
    }
    return HttpResponse(template.render(context, request))


def Courts(request):
    courts = Court.objects.all()
    template = loader.get_template('home/Court/Courts.html')
    context = {
        'courts': courts,
    }
    return HttpResponse(template.render(context, request))


# Edit Court
def edit_Court(request, id):
    court = get_object_or_404(Court, id_court=id)

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
            court.schedule_type = form.cleaned_data['schedule_type']
            court.min_duration_months = form.cleaned_data['min_duration_months']
            court.total_hours_per_month = form.cleaned_data.get('total_hours_per_month', None)
            court.save()
            return redirect('Courts')
    else:
        form = CourtEditForm(court=court)

    return render(request, 'home/Court/Court-edit.html', {'form': form, 'court': court})


# Add a new court
def CourtNew(request):
    if request.method == "POST":
        form = CourtNewForm(request.POST)
        print("Dữ liệu POST:", request.POST)

        if form.is_valid():
            # Lưu thủ công vào database vì Form không có .save()
            Court.objects.create(
                name_court=form.cleaned_data["name_court"],
                location=form.cleaned_data["location"],
                start_time=form.cleaned_data["start_time"],
                end_time=form.cleaned_data["end_time"],
                status=form.cleaned_data["status"],
                type_court=form.cleaned_data["type_court"],
                cost_court=form.cleaned_data["cost_court"],
                schedule_type=form.cleaned_data["schedule_type"],
                min_duration_months=form.cleaned_data["min_duration_months"],
                total_hours_per_month=form.cleaned_data.get("total_hours_per_month", None)
            )
            
            messages.success(request, "Sân cầu lông đã được thêm thành công!")
            print("Saved successfully!")
            return redirect("Courts")
        else:
            print("Lỗi form:", form.errors)
            messages.error(request, "Có lỗi xảy ra. Vui lòng kiểm tra lại thông tin.")
    
    else:
        form = CourtNewForm()

    return render(request, 'home/Court/Court-new.html', {'form': form})


# Delete court
def delete_court(request, court_id):
    print(f"Nhận yêu cầu xóa sân ID: {court_id}")
    if request.method == "POST":
        try:
            court = get_object_or_404(Court, id_court=court_id)
            court.delete()
            print(f"Đã xóa sân {court_id}")
            return JsonResponse({"success": True})
        except Exception as e:
            print(f"Lỗi khi xóa sân: {e}")
            return JsonResponse({"success": False, "error": str(e)}, status=500)
    return JsonResponse({"success": False, "error": "Invalid request"}, status=400)


# List all Payments
def Bookings(request):
    Bookings = Booking.objects.all()  # Fixed variable naming
    template = loader.get_template('home/Booking/Bookings.html')
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
    # Debug: Kiểm tra dữ liệu nhận từ URL
    print("GET parameters:", request.GET)

    if request.method == "POST":
        form = BookingNewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/Bookings")  # Điều hướng sau khi đặt sân
    else:
        form = BookingNewForm(initial={
            'name_court': request.GET.get('name_court', ''),
            'start_time': request.GET.get('start_time', ''),
            'end_time': request.GET.get('end_time', ''),
            'cost_court': request.GET.get('cost_court', ''),
            'type_court': request.GET.get('type_court', ''),
            'location': request.GET.get('location', ''),
        })

    return render(request, 'home/Booking/Booking-new.html', {'form': form})
