# Generated by Django 2.2.2 on 2019-07-17 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spr_User',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', max_length=20)),
                ('email', models.CharField(db_column='email', max_length=30)),
                ('phone', models.CharField(blank=True, db_column='phone', max_length=13)),
            ],
            options={
                'db_table': 'spr_user',
                'managed': False,
            },
        ),
    ]
