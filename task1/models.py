from django.db import models


# Create your models here.
class Signup1(models.Model):
    username = models.CharField(max_length=250)
    join_date = models.DateTimeField(auto_now_add=True)
    phone_no =models.CharField(max_length=250)
    password = models.CharField(max_length=100)


    def __str__(self):
        return self.username

class Task(models.MOdel):
    