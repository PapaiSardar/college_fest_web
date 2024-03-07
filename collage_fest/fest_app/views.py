from django.shortcuts import render
from django.http import HttpResponse
from fest_app.models import *

# Create your views here.
def login(request):
    return render(request,'login.html')

def events(request):
    return render (request,'events.html')


def events_regis(request):
    return render (request,'event_regis.html')

def home(request):
    return render(request,'index.html')
def student_login(request):
    return render(request,'stu_login.html')

def s_login(request):
    u=student_basic()
    u.name=request.GET['a1']
    u.roll=request.GET['a2']
    a=request.GET['a3']
    u.payment_status=0
    z=request.GET['college']
    if z=="Future Institute of Technology":
        u.college_name=z
    else:
        u.college_name=a
    u.collage_status=0
    u.save()
    return render(request,'stu_login.html')