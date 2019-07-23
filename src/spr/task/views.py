from django.shortcuts import render,redirect
from .models import Task
from django.views import View


class index(View):
    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()

        context = {
            "tasks":tasks,
        }
        return render(request, 'task.html', context)
