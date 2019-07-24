from django.shortcuts import render,redirect
from .models import Task
from django.views import View


class index(View):

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()

        context = {
            "tasks":tasks,
        }
        return render(request, 'task_list.html', context)

    def create_task(self, request):
        if request.method == 'POST':
            if request.POST.get('title') and request.POST.get('content'):
                task = Task()
                task.title = request.POST.get('title')                
                task.due_date = request.POST.get('due_date')
                task.priority = request.POST.get('priority')
                task.sub_task = request.POST.get('sub_task')
                task.status = request.POST.get('status')
                task.save()
                
                return render(request, 'task.html')


