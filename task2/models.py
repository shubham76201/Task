from django.db import models

# Create your models here.

class hieracy1(models.Model):
    title = models.CharField(max_length=200)
    parent_id=models.CharField(max_length=100)


    def __str__(self):
        return self.title