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



def p_status(request):
    return render(request,'payment_check.html')



def pay_check(request):
    a=request.GET['a1']
    if a in student_detalis.objects.filter(roll=a):
        u=student_detalis.objects.get(roll=a)
        if u.payment_status==1:
            return render(request,'payment_check.html',{'c':'payment clear'})
        elif u.payment_status==0:
            return render(request,'payment_check.html',{'c':'Payment not clear if you already pay plese please call 7470255315'})
        else:
            return render(request,'payment_check.html',{'c':'data not found reg. please'})
    else:
        return render(request,'stu_login.html')
    



def check_payment(request):
    
    if request.method == 'POST':
        roll = request.POST.get('roll')  # Assuming roll is submitted via POST
        
        try:
            student = student_detalis.objects.get(roll=roll)
            if student.payment_status == 1:
                payment_status = "Payment is completed."
            else:
                payment_status = "Payment is not completed.If your payment is already done please call 7470255315."
        except student_detalis.DoesNotExist:
            return render(request,'stu_login.html')
            # payment_status = "Student with this roll number does not exist."

        return render(request, 'payment_status.html', {'payment_status': payment_status})
    else:
        return render(request, 'payment_status.html')