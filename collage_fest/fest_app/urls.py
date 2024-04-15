from django.urls import path
from . import views
urlpatterns=[
    path("",views.home,name='home'),
    path("home",views.home),
    path('student_login',views.student_login),
    path('s_login',views.s_login),
    path('events/',views.events,name='events'),
    path('events_regis/',views.events_regis,name ='events_regis'),
    path('login_stu',views.login_stu),
    path('payment_status',views.p_status),
    path('check_payment',views.check_payment),
    #path('check-payment/', views.check_payment, name='check_payment'),
    path('admin_login',views.admin_login),
    path('ad_log',views.ad_log),
    path('log_app',views.log_app),
    path('l_app/<int:id>',views.l_app),
    path('pay_app',views.py_app),
    path('p_app/<int:id>',views.p_app),
    path('login/', views.custom_login, name='login'),
    path('logout_page/', views.logout_page,name='logout_page'),
    path('QR_page',views.QR_page),
    path('submit',views.submit),
    path('add_event',views.add_event),
    path('event_add',views.event_add),


    
    path('save_data/', views.save_data, name='save_data'),
    path('logout/', views.logout, name='logout'),
    path('logout_page/events', views.events),
    path('logout_page/save_data/', views.save_data),
    # path('events_regis',views.events_regis),
    
]