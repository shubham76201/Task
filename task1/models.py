from django.db import models


# Create your models here.
class Signup1(models.Model):
    username = models.CharField(max_length=250)
    join_date = models.DateTimeField(auto_now_add=True)
    phone_no =models.CharField(max_length=250)
    password = models.CharField(max_length=100)


    def __str__(self):
        return self.username

class Task(models.Model):
    uid=models.ForeignKey(Signup1,on_delete=models.CASCADE,default=1)
    task_title=models.CharField(max_length=200)
    task_description=models.CharField(max_length=2000,null=True)
    task_pic=models.URLField()
    task_time_stamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.task_title
