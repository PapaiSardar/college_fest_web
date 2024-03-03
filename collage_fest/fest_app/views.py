from django.shortcuts import render
from django.http import HttpResponse
from fest_app.models import *

# Create your views here.
def login(request):
    return render(request,'login.html')

def home(request):
    return render(request,'index.html')
