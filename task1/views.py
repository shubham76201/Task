from django.db.models.fields import AutoField
from task1.models import Signup1
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.contrib import auth
from .models import Signup1, Task
from rest_framework import viewsets

from .serializer import TaskSerializer

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
        if (first_char=="a" or first_char=="A") :
          obj = Signup1(username=username,password=password1,phone_no=phone)
          obj.save()
          print("User Created")
          return render(request,'task.html')
        
        else:
            return render(request,'wrong.html')
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
def exp(request):
        new1=Signup1.objects.all
        #new2=Signup1.objects.get(username=new1).id
        
        return render(request,'sample.html',{'new1':new1})
def task_details(request):
    if request.method=="POST" and request.FILES['myfile']:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            image2 = fs.url(filename)
            title=request.POST['title']
            des = request.POST['des']
            
            all_uploads=Task(task_title=title ,task_pic=image2,task_description=des)
            all_uploads.save()
            task1=Task.objects.get(task_title=title).task_time_stamp
            task2=Task.objects.get(task_title=title).id
            
            return render(request, 'result.html',{'title':title,'des':des,'image':image2,'task':task1,'task2':task2})

            
    else:
        return render(request,'task.html')

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('task_title')
    serializer_class = TaskSerializer