from django.db import models
from django.utils import timezone
from user.models import User

# Create your models here.
class TodoList(models.Model):
    id = models.CharField(db_column='id', primary_key=True, max_length=8)
    title = models.CharField(max_length=250)
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    completed = models.BooleanField(default=False)
    in_progress = models.BooleanField(default=False)
    priority = models.PositiveIntegerField(blank=True, null=True)
    user_id = models.ForeignKey(User, models.CASCADE, db_column='user_id')

    class Meta:
        managed = False
        db_table = 'todolist'
