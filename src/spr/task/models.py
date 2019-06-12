from django.db import models
from django.utils import timezone

# Create your models here.
class TodoList(models.Model):
    title = models.CharField(max_length=250)
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
