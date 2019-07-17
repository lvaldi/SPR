from django.shortcuts import render,redirect
from .models import *
from django.views import View


class index(View):
    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        task_milestones = Task_Milestones.objects.all()

        context = {
            "tasks":tasks,
            "task_milestones":task_milestones
        }
        return render(request, 'task.html', context)
