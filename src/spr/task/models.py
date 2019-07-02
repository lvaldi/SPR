from django.db import models
from django.utils import timezone
from user.models import User


# Create your models here.
class TodoList(models.Model):

    id = models.CharField(db_column='id', primary_key=True, max_length=8)
    title = models.CharField(max_length=50)
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    priority = models.CharField(max_length=1, choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')])

    class Meta:
        managed = False
        db_table = 'todolist'

class Milestone(models.Model):

    INCOMPLETE = '0'
    IN_PROGRESS = '1'
    COMPLETED = '2'
    STATUS = [(INCOMPLETE, 'Incomplete'), (IN_PROGRESS, 'In Progress'), (COMPLETED, 'Completed')]

    id = models.CharField(db_column='id', primary_key=True, max_length=8)
    task_id = models.ForeignKey('TodoList', models.CASCADE, db_column="task_id")
    description = models.CharField(db_column='description', max_length=200, null=False)
    status = models.CharField(max_length=1, choices=STATUS, default=INCOMPLETE)
    ordering = models.CharField(db_column='ordering', max_length=5, null=False)
    
    class Meta:
        managed = False
        db_table = 'milestone'
        ordering = ['id', 'task_id']
