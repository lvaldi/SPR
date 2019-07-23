from django.db import models
from django.utils import timezone

# Create your models here.

class Task(models.Model):

    id = models.AutoField(db_column='id', primary_key=True, max_length=8)
    title = models.CharField(db_column='title', max_length=500, null=True)
    due_date = models.DateField(db_column='due_date', null=True)
    priority = models.CharField(db_column='priority', max_length=20, choices=[(
        'Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], blank=False, null=True)
    sub_task = models.CharField(db_column='sub_task', max_length=500, null=True)
    status = models.CharField(db_column='status', max_length=30, choices=[(
        'Incomplete', 'Incomplete'), ('In Progress', 'In Progress'), ('Complete', 'Completed')], blank=False, null=True)
    parent_task = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='task')

    class Meta:
        db_table = 'task'