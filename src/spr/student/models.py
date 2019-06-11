from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.TextField()
    id = models.TextField(primary_key=True)
