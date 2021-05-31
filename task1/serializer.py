from rest_framework import serializers

from .models import Task

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('url','uid', 'task_title','task_description','task_pic','task_time_stamp')