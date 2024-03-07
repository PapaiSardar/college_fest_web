from django.urls import path
from . import views
urlpatterns=[
    path("",views.login),
    path('home',views.home),
    path('student_login',views.student_login),
    path('s_login',views.s_login),
    path('events',views.events),
    path('event_regis',views.event_regis),

]