from django.contrib import admin

# Register your models here.
from .models import Task, Task_Milestones

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'due_date', 'priority_value')

class Task_MilestonesAdmin(admin.ModelAdmin):
    list_display = ('id', 'task_id', 'milestone', 'status_value')

admin.site.register(Task, TaskAdmin)
admin.site.register(Task_Milestones, Task_MilestonesAdmin)