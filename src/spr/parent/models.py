from django.db import models

# Create your models here.
class Parent(models.Model):
    name = models.CharField(db_column="name", max_length=20, null=False)
