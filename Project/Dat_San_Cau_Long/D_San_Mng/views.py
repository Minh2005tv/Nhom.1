from django.shortcuts import render
from django.http import HttpResponse

def Customer(request):
    return HttpResponse("Hello world!")
                        
def Booking(request):
    return HttpResponse("Hello world!")

def Payment(request):
    return HttpResponse("Hello world!")

def Court(request):
    return HttpResponse("Hello world!")

