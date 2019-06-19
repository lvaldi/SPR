from django.db import models
from django.utils import timezone
from student.models import Student
from parent.models import Parent
from mentor.models import Mentor

# Create your models here.
class TodoList(models.Model):
    id = models.CharField(db_column='id', primary_key=True, max_length=8)
    title = models.CharField(max_length=250)
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    completed = models.BooleanField(default=False)
    in_progress = models.BooleanField(default=False)
    priority = models.PositiveIntegerField(blank=True, null=True)
    mid = models.ForeignKey(Mentor, models.CASCADE, db_column='mid')
    sid = models.ForeignKey(Student, models.CASCADE, db_column='sid')
    pid = models.ForeignKey(Parent, models.CASCADE, db_column='pid')

    class Meta:
        managed = False
        db_table = 'todolist'
        unique_together = (('mid', 'sid', 'pid'),)
