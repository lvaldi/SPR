from django.db import models

# Create your models here.
class Mentor(models.Model):
    name = models.TextField()
    id = models.AutoField(primary_key=True)
