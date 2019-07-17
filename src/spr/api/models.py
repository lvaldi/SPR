from tastypie.resources import ModelResource
from task.models import Task_Milestones

# Create your models here.

class TaskResource(ModelResource):

    class meta:
        queryset = Task_Milestones.objects.all()
        resource_name = 'task'
