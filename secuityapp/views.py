from django.shortcuts import render,redirect
from .models import UserReg,Profile,Job
from django.http import HttpResponse
from django.utils.dateparse import parse_date
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
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
          res = HttpResponse(status=302)
          if request.POST.get('chk'):
            res.set_cookie('ukey',obj.email)
            res.set_cookie('upass',obj.password)
         
          request.session["ukey"]=obj.email 
          res['Location']='/secuityapp/user-dashboard'   
          return res
    else:
      c1=''
      c2=''  
      if request.COOKIES.get('ukey'):
        c1=request.COOKIES["ukey"]
        c2=request.COOKIES["upass"]
      return render(request,"secuityapp/login.html",{'username':c1,'pass':c2})

def userdashboard(request):
    if request.session.has_key("ukey"):
       udata = request.session.get("ukey")
       chkprofile = Profile.objects.filter(email=udata).first()
       if chkprofile!=None:
          data = Profile.objects.filter(email=udata) 
          return render(request,"secuityapp/userdashboard.html",{"key":udata,"profile":data})
       else:
          return render(request,"secuityapp/addprofile.html")
    else:
       return redirect('/secuityapp/user-login') 
def saveprofile(request):
    if request.method=="POST":
        obj = Profile(aboutme=request.POST.get("about"),hobby=request.POST.get("hobby"),email=request.session.get("ukey"),createdate= parse_date(request.POST.get("cdate")))
        obj.save()
        return redirect('/secuityapp/user-dashboard')
    
def userlogout(request):
    del request.session["ukey"]
    return redirect('/secuityapp/user-login') 
def usercookie(request):
    response = HttpResponse("Cookie Set")
    response.set_cookie('ckey', 'hello',max_age=10)
    return response
def getcookie(request):
     a  = request.COOKIES['ckey']
     return HttpResponse("Cookie data is "+a)
def deletecookie(request):
    response = HttpResponse("Cookie Set")
    response.delete_cookie('ckey')
    return response
class JobCreate(CreateView):
    model = Job
    fields = ['jobtitle', 'jobdescription']
    success_url='/secuityapp/joblist'
class JobList(ListView):
     model = Job   # Job.objects.all()   