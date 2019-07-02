from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(db_column="id", primary_key=True)
    name = models.CharField(db_column="name", max_length=20, null=False)
    email = models.CharField(db_column="email", max_length=30, null=False)
    phone = models.CharField(db_column="phone", max_length=13, null=False, blank=True)

    class Meta:
        managed = False
        db_table = 'user'

