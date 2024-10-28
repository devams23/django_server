from django.shortcuts import render , HttpResponse
from newapp.models import Services
from datetime import datetime
from django.contrib import messages
# Create your views here.
def index (request):
    context = {
        "var1" : "hello",
        "var2"  : "world"
    }
    return render(request,  'base.html' , context)

def about(request):
    return render(request ,  'about.html')


def home(request):
    return render(request , 'home.html')

def aftersub(request):
    return render(request , 'aftersub.html')

def services(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        zipp = request.POST.get('zipp')
        city = request.POST.get('city')
        ser = Services(email = email , password = password , zipp = zipp , city = city )
        ser.save()
        messages.success(request, 'Form submitted succesfully!')
    return render(request , 'services.html')
# def sevices(request):
#     return HttpResponse('this is sevices page')

