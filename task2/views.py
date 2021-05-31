from task2.models import hieracy1
from django.shortcuts import render
from task2.models import hieracy1
from django.shortcuts import render,redirect

# Create your views here.
def task12(request):
    parentid_list=[]
    title_list=[]
    new1=hieracy1.objects.all()
    a1=len(new1)
    a1=len(new1)+1
    res={}
    for a in range(1,a1):
       a4=hieracy1.objects.get(id=a).parent_id
       a5=hieracy1.objects.get(id=a).title
       parentid_list.append(a4)  
       title_list.append(a5)  
    # List to Dictionary
    res = dict(zip(title_list, parentid_list))
    res1 = dict(zip(title_list, parentid_list))
    print(res)
    a6=[]
    count_list=[]
    null_list=[]
    non_null=[]
    main=[]
    # for the Null Values 
    count=0
    for i in res:
        count=count+1
        x=res[i]
        a6.append(x)
        main.append(i)
        # Null List for Null values 

        if x=='Null':
            count_list.append(count)
            null_list.append(i)
        else:
            non_null.append(i)
    print("Index of Null Values: ",count_list)
    print("List of Null Keys : ",null_list)
    print("List of Non-Null Keys : ",non_null)
    print("List of Keys List : ",main)
    
    Two=[]
    Three=[]
    
    for i in null_list:
        del res1[i]
    print("List of the Non-NUll Values : ",res1)
    count123=0
    for i in res.values():
       count123=count123+1
       if i=='2':
           Two.append(main[count123-1])
       if i=='3':
           print(count123)
           
           Three.append(main[count123-1])   
    #        a=count_list[i]
    #        Two.append(a)
    #    elif i=='3':
    #        Three.append(count_list[i])
    print(Two)
    print(Three)
    return render(request,'task2.html',{'Null':null_list,'Two':Two,'Three':Three}) 