from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from fest_app.models import *
from django.http import Http404
import json

# Create your views here.
def events(request):
    return render (request,'events.html')

def save_data(request):
    if request.method == 'POST':
        roll = 342  # Predefined roll number
        eventname = request.POST.get('event_name')
        try:
            student = student_detalis.objects.get(roll=roll)
        except student_detalis.DoesNotExist:
            raise Http404("Student does not exist")

        # Check if a record with the roll number already exists
        try:
            z = abc.objects.get(roll=roll)
        except abc.DoesNotExist:
            # If the roll number is not in the table, create a new record
            z = abc(roll=roll)

        # Map event names to field names
        event_field_map = {
            'CatWalk': 'CatWalk',
            'DuoDance': 'DuoDance',
            'mintoframe': 'mintoframe',
            'Facepaint': 'Facepaint',
            'rell': 'rell',
            'selfie': 'selfie'
        }

        # Set the event to 1 based on the event_name
        if eventname in event_field_map:
            setattr(z, event_field_map[eventname], 1)

        # Assuming the field names are the same as the event names in your event_field_map
        l = [event_name for event_name, field_name in event_field_map.items() if getattr(z, field_name) == 1]

        
        z.save()

        return render(request, 'event_regis.html', {'l': l,'student': student})
    else:
        return HttpResponse('Invalid request method')
    
    

#     return render(request, 'event_regis.html', {'student': student})

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
    


def admin_login(request):
    return render(request,'admin_login.html')
def ad_log(request):
    a=request.GET['roll']
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


def QR_page(request):
    return render(request,'QR_PAGE.html')




def submit(request):
    html_content = """
    <html>
    <head>
        <title>My Page</title>
    </head>
    <body>
        <h1>Payment Done ! it'll take few minute to updates the payment status </h1>
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

# def save_data(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             roll = data.get('roll')
#             event_name = data.get('event_name')
#             if roll and event_name:  # Validate form data
#                 event.objects.create(roll=roll, event_name=event_name)
#                 return JsonResponse({'message': 'Data saved successfully'})
#             else:
#                 return JsonResponse({'error': 'Invalid form data'})
#         except Exception as e:
#             return JsonResponse({'error': str(e)})
#     else:
#         return JsonResponse({'error': 'Invalid request method'})



    
# def event_list(request):
#     # Get all records where the event value is 1
#     e = abc.objects.get(roll=34230821042)

#     # Extract the event names
#     event_names = []
#     for event in e:
#         if event.CatWalk == 1:
#             event_names.append('CatWalk')
#         if event.DuoDance == 1:
#             event_names.append('DuoDance')
#         if event.mintoframe == 1:
#             event_names.append('mintoframe')
#         if event.Facepaint == 1:
#             event_names.append('Facepaint')
#         if event.rell == 1:
#             event_names.append('rell')
#         if event.selfie == 1:
#             event_names.append('selfie')

#     print(event_names)

#     return render(request, 'event_regis', {'event_names': event_names})