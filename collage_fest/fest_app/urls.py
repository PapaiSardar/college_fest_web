from django.urls import path
from . import views
urlpatterns=[
    path("",views.home),
    path("home",views.home),
    path('student_login',views.student_login),
    path('s_login',views.s_login),
    path('events',views.events),
    path('events_regis',views.events_regis),

]