from imaplib import _Authenticator
from multiprocessing import AuthenticationError
from operator import index
from telnetlib import AUTHENTICATION, LOGOUT
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django. http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
# Create your views here.
def home(request):
    return render(request,"index1.html")
def index(request):
    return render(request,"index.html")


def signup(request):
    if request.method=="POST":

     # username=request.POST.get('username')
       username = request.POST['username']
       fname = request.POST['fname']
       lname = request.POST['lname']
       email = request.POST['email']
       pass1 = request.POST['pass1']
       pass2= request.POST['pass2']

       myuser=User(username=username,email=email,password=pass1,first_name=fname,last_name=lname)
       

       myuser.save()
       messages.success(request,"your account has been succesfully created")

       return redirect('signin')
    
    return render(request,"signup.html")

def signin(request):

    if request.method=='POST':
     username=request.POST['username']
     pass1=request.POST['pass1']
     
     user= authenticate(username=username,password=pass1)

     if user is not None:
         login(request,user)
         fname=user.first_name
         return render(request,"index.html",{'fname':fname})
     else:
         messages.error(request,"Bad credentials!")
         return redirect('index')
    return render(request,"signin.html")
    
def signout(request):
    LOGOUT(request)
    messages.success(request,"logged out successfully")
    return redirect('home')