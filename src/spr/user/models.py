from django.db import models

# Create your models here.

class User(models.Model):
    id = models.CharField(db_column='id', primary_key=True, max_length=8)
    name = models.CharField(db_column="name", max_length=50, null=False)
    role = models.CharField(db_column="role", max_length=20, null=False)

    class Meta:
        managed = False
        db_table = 'user'
