from django.db import models
from tastypie.resources import ModelResource
from task.models import Task

class TaskResource(ModelResource):
    class Meta:
        queryset = Task.objects.all()
        resource_name = 'tasks'