from django.db.models.fields import AutoField
from task1.models import Signup1
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Signup1

# Create your views here.
def signup(request):
    if request.method=="POST":
        username= request.POST.get('username1')
        phone= request.POST.get('phone')
        password= request.POST.get('password')
        # for the Hashed Password
        password1=make_password(password)
        first_char=username[0]
        last_char = username[-1]
        print(first_char)
        print(last_char)

        obj = Signup1(username=username,password=password1,phone_no=phone)
        
        obj.save()
        print("User Created")
        return redirect('/')

    else:
      return render(request,'signup.html')

def signin(request):
    if request.method=="POST":
        username= request.POST.get('username1')
        password= request.POST.get('password')
        # for the Hashed Password
        signin1=Signup1.objects.get(username=username).password
        print(signin1)
        print(password)
        password2=check_password(password,signin1)
        print(password2)
        # Hashing and checking Done 
        if password2==True:
             return redirect('/')
        else :
             print("Wrong Password")

    else:
      return render(request,'signin.html')
