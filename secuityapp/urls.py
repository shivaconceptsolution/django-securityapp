from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('services',views.services,name='services'),
    path('guards',views.guards,name='guards'),
    path('contactus',views.contactus,name='contactus'),
    path('user-registration',views.userreg,name='userreg'),
    path('user-login',views.userlogin,name='userlogin'),
    path('user-dashboard',views.userdashboard,name='userdashboard'),
    path('user-logout',views.userlogout,name='userlogout'),
]