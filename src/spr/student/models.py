from django.db import models

# Create your models here.
class Student(models.model):
    name = models.TextField()
    id = models.TextField()
