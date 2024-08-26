from django.shortcuts import render,redirect
from .models import UserReg
def home(request):
    return render(request,"secuityapp/index.html")
def aboutus(request):
    return render(request,"secuityapp/about.html")
def services(request):
    return render(request,"secuityapp/service.html")
def contactus(request):
    return render(request,"secuityapp/contact.html")
def guards(request):
    return render(request,"secuityapp/guard.html")
def userreg(request):
    if request.method=="POST":
        obj = UserReg(email=request.POST.get("email"),password=request.POST.get("password"),fullname=request.POST.get("fname"),mobileno=request.POST.get("mobile"),address=request.POST.get("address"))
        obj.save()
        return redirect('/secuityapp/user-login')
    return render(request,"secuityapp/reg.html")
def userlogin(request):
    if request.method=="POST":
        obj = UserReg.objects.filter(email=request.POST.get("email"),password=request.POST.get("password")).first()
        if obj!=None:
           request.session["ukey"]=obj.fullname
           return redirect('/secuityapp/user-dashboard')
    return render(request,"secuityapp/login.html")

def userdashboard(request):
    if request.session.has_key("ukey"):
       udata = request.session.get("ukey")
       return render(request,"secuityapp/userdashboard.html",{"key":udata})
    else:
       return redirect('/secuityapp/user-login') 
def userlogout(request):
    del request.session["ukey"]
    return redirect('/secuityapp/user-login') 