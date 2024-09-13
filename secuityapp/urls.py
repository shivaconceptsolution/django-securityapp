from django.urls import path
from . import views
from .views import JobCreate,JobList
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
    path('user-cookie',views.usercookie,name='usercookie'),
    path('get-cookie',views.getcookie,name='getcookie'),
    path('delete-cookie',views.deletecookie,name='deletecookie'),
    path('save-profile',views.saveprofile,name='saveprofile'),
    path('jobcreate',JobCreate.as_view()),
    path('joblist',JobList.as_view()),
    path('upload-file',views.uploadfile,name='uploadfile'),
    path('viewfile',views.viewfile,name='viewfile'),
    path('ajaxsearch',views.ajaxsearch,name='ajaxsearch'),
    path('ajaxcode',views.ajaxcode,name='ajaxcode'),
    path('ajaxcodenew',views.ajaxcodenew,name='ajaxcodenew'),
    path('checkemailfun',views.checkemailfun,name='checkemailfun'),


]