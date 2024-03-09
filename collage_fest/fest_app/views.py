from django.shortcuts import render
from django.http import HttpResponse
from fest_app.models import *
from django.http import Http404

# Create your views here.
def events(request):
    return render (request,'events.html')


def events_regis(request):
    try:
        student = student_detalis.objects.get(roll=34230821020)
    except student_detalis.DoesNotExist:
        raise Http404("Student does not exist")
    
    return render(request, 'event_regis.html', {'student': student})

def home(request):
    return render(request,'index.html')
def student_login(request):
    return render(request,'stu_login.html')

def s_login(request):
    u=student_detalis()
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
    return render(request,'thank_reg.html')


def login_stu(request):
    return render(request,'login.html')