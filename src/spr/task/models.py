from django.db import models
from django.utils import timezone

# Create your models here.

class Task(models.Model):

    id = models.AutoField(db_column='id', primary_key=True, max_length=8)
    title = models.CharField(db_column='title', max_length=50)
    due_date = models.DateField(db_column='due_date', null=False)
    priority = models.CharField(db_column='priority', max_length=20, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], blank=False, null=False)

    class Meta:
        db_table = 'task'

    def priority_value(self):
        return self.priority

class Task_Milestones(models.Model):

    STATUS = [('Incomplete', 'Incomplete'), ('In Progress', 'In Progress'), ('Complete', 'Completed')]
    id = models.CharField(db_column='id', primary_key=True, max_length=8)
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE, db_column='task_id', max_length=8)
    milestone = models.CharField(db_column='milestone', max_length=200, null=False)
    objects = models.Manager()

    status = models.CharField(db_column='status', max_length=30, choices=STATUS, default="Incomplete")

    class Meta:
        db_table='task_milestone'
        unique_together = ['id', 'task_id']
        ordering = ['task_id', 'id']  # sort by task_id then id

    def status_value(self):
        return self.status
