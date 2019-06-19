from django.db import models

# Create your models here.
class Mentor(models.Model):
    id = models.CharField(db_column='id', primary_key=True, max_length=8)
    name = models.CharField(db_column="name", max_length=20, null=False)

    class Meta:
        managed = False
        db_table = 'mentor'