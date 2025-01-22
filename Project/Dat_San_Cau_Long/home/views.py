# views.py
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from D_San_Mng.models import Court, Payment
from .forms import CourtNewForm, PaymentNewForm


# Home view
def home(request):
    return render(request, 'home/index.html')


# List all Payments
def Payments(request):
    payments = Payment.objects.all()  # Fixed variable naming
    template = loader.get_template('home/Payments.html')
    context = {
        'payments': payments,  # Updated context key
    }
    return HttpResponse(template.render(context, request))


# Edit a Payment
def edit_Payment(request, id):
    payment = get_object_or_404(Payment, id=id)  # Use get_object_or_404 for error handling
    template = loader.get_template('home/Payment-edit.html')
    context = {
        'payment': payment,  # Fixed variable name
    }
    return HttpResponse(template.render(context, request))


# Create a New Payment
def PaymentNew(request):
    if request.method == "POST":
        form = PaymentNewForm(request.POST)
        if form.is_valid():
            # Create and save the Payment instance
            payment = Payment(
                payment_id=form.cleaned_data['payment_id'],
                booking=form.cleaned_data['booking'],
                customer=form.cleaned_data['customer'],
                payment_date=form.cleaned_data['payment_date'],
                active=form.cleaned_data['active'],
            )
            payment.save()
            return HttpResponseRedirect("/Payments")
    else:
        form = PaymentNewForm()

    template = loader.get_template('home/Payment/Payment-new.html')  # Check this path
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))

# List all Courts
def Courts(request):
    courts = Court.objects.all()  # Fixed variable naming
    template = loader.get_template('home/Courts.html')
    context = {
        'courts': courts,  # Updated context key
    }
    return HttpResponse(template.render(context, request))

def edit_Court(request, id=None): 
    if id:
        court = get_object_or_404(Court, id=id) 
        context = {'court': court} 
    else: 
        context = {'message': 'No Court selected for editing.'} 
        template = loader.get_template('home/Court-edit.html') 
        return HttpResponse(template.render(context, request))

def CourtNew(request):
    if request.method == "POST":
        form = CourtNewForm(request.POST)
        if form.is_valid():
            # Create and save the Payment instance
            court = Court(
                name_court=form.cleaned_data['name_court'],
                start_time=form.cleaned_data['start_time'],
                end_time=form.cleaned_data['end_time'],
                status=form.cleaned_data['status'],
                type_court=form.cleaned_data['type_court'],
                cost_court=form.cleaned_data['cost_court'],
            )
            court.save()
            return HttpResponseRedirect("/Courts")
    else:
        form = PaymentNewForm()

    template = loader.get_template('home/Court/Court-new.html')  # Check this path
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))