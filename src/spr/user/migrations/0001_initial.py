# Generated by Django 2.2.2 on 2019-06-18 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.CharField(db_column='id', max_length=8, primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', max_length=20)),
            ],
            options={
                'db_table': 'student',
                'managed': False,
            },
        ),
    ]