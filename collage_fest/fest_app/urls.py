from django.urls import path
from . import views
urlpatterns=[
    path("",views.login),
    path('home',views.home),
    path('student_login',views.student_login),
]