from django.shortcuts import render,redirect
from django.http import HttpResponse
from fest_app.models import *
from django.http import Http404
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
import os

# Create your views here.
def events(request):
    return render (request,'events.html')


def events_regis(request):
    try:
        student = student_detalis.objects.get(roll=34230821042)
    except student_detalis.DoesNotExist:
        raise Http404("Student does not exist")
    
    return render(request, 'event_regis.html', {'student': student})

def home(request):
    return render(request,'index.html')
def student_login(request):
    return render(request,'stu_login.html')

def s_login(request):
    u=student_detalis()
    if request.method == 'POST':
        u.name=request.POST.get('a1')
        u.roll=request.POST.get('a2')
        s=str(request.FILES['icard'])
        a=request.POST['a3']
        z=request.POST.get('college')
    if z=="Future Institute of Technology":
        u.college_name=z
    else:
        u.college_name=a
    handle_uploaded_file(request.FILES['icard'],s)
    url="upload/"+s
    u.id_card=url
    u.collage_status=0
    u.payment_status=0
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
    


def admin_login(request):
    return render(request,'admin_login.html')
def ad_log(request):
    if request.method=="POST":

        a=request.POST['password']
        if a=='arnab@2003':
            condition = True
        else:
            condition = False
    
    context = {'condition': condition}
    return render(request, 'admin_login.html', context)


def log_app(request):
    students = student_detalis.objects.filter(collage_status=0)
    return render(request, 'student_list.html', {'students': students})


def l_app(request,id):
    u=student_detalis.objects.get(id=id)
    u.collage_status=1
    u.save()
    return redirect("../log_app")


def py_app(request):
    students = student_detalis.objects.filter(payment_status=0)
    return render(request, 'student_list1.html', {'students': students})



def p_app(request,id):
    u=student_detalis.objects.get(id=id)
    u.payment_status=1
    u.save()
    return redirect("../pay_app")



def custom_login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        roll = request.POST.get('roll')
        user = authenticate(request, name=name, roll=roll)
        if user is not None:
            # Authentication successful, log the user in
            auth_login(request, user)  # Use auth_login instead of login
            return redirect('home')  # Redirect to home page after login
        else:
            # Authentication failed, show error message
            messages.error(request, 'Invalid name or roll number')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')


 # Redirect to login page after logout


def QR_page(request):
    return render(request,'QR_PAGE.html')





def submit(request):
    html_content = """
    <html>
    <head>
        <title>My Page</title>
    </head>
    <body>
        <h1>Payment Done ! it'll take 24 hours to updates the payment status </h1>
        <p>Click <a href="home">here</a> to return HOME page</p>
    </body>
    </html>
    """


    response = HttpResponse(html_content)

    return response

def add_event(request):
    return render(request,'event_det.html')

def event_add(request):
    z=events_detalis()
    z.event_id=request.GET['a1']
    z.event_name=request.GET['a2']
    z.part_no=0
    z.save()
    return render(request,'event_det.html')
def handle_uploaded_file(file,file_name):
    if not os.path.exists('fest_app/static/upoad'):
        os.mkdir('fest_app/static/upoad')
    with open('fest_app/static/upoad/'+file_name, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

