# Generated by Django 2.2.2 on 2019-06-11 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('name', models.TextField()),
                ('id', models.TextField(primary_key=True, serialize=False)),
            ],
        ),
    ]
