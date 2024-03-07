from django.shortcuts import render
from django.http import HttpResponse
from fest_app.models import *

# Create your views here.
def login(request):
    return render(request,'login.html')

def events(request):
    return render (request,'events.html')
def event_regis(request):
    return render(request,'event_regis.html')

def home(request):
    return render(request,'index.html')
def student_login(request):
    return render(request,'stu_login.html')
def s_login(request):
    u=student_basic()
    u.name=request.GET['a1']
    u.roll=request.GET['a2']
    u.payment_status=0
    u.save()
    return render(request,'stu_login.html')