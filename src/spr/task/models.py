from django.db import models
from django.utils import timezone
from user.models import User


# Create your models here.
class TodoList(models.Model):
    id = models.CharField(db_column='id', primary_key=True, max_length=8)
    title = models.CharField(max_length=250)
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    status = models.CharField(max_length=1, choices=[(0, 'Incomplete'), (
        1, 'In Progress'), (2, 'Completed')], default=0)
    priority = models.CharField(max_length=1, choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')])
    milestone = models.TextField()
    # user_id = models.ForeignKey(User, models.CASCADE, db_column='UID')

    class Meta:
        managed = False
        db_table = 'todolist'
