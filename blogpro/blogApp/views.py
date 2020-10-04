
from django.shortcuts import render,redirect,HttpResponse
from .forms import UserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

def home(request):
    userName=request.session.get('userName')
    return render(request,"index.html")


def addUser(request):
   
    if request.method=='POST':
        u=UserForm(request.POST)
        u.save()
        return redirect("/")
    else:
        u=UserForm
        return render(request,'myform.html',{'form':u})

    
def mylogin(request):

    if request.method=='POST':
        uname=request.POST.get("uname")
        passw=request.POST.get("passw")
        usr=authenticate(request,username=uname,password=passw)
        if usr is not None:
            request.session['userName']=uname
            login(request,usr)
            return redirect("/")
        else:
            return HttpResponse("<h1>Invalid UserName and Passwor</h1>")
    else:
        return render(request,'login.html')
    
def logOUT(request):
    logout(request)
    return redirect("/")

def myblog(request):
    return render(request,"blog.html")

def beaches(request):
    return render(request,"beaches.html")

def fort(request):
    return render(request,"fort.html")

def hill(request):
    return render(request,"hill.html")

