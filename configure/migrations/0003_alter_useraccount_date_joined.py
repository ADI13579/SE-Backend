# Generated by Django 4.0.1 on 2022-01-21 07:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ocw', '0002_alter_useraccount_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='date_joined',
            field=models.DateField(default=datetime.datetime(2022, 1, 21, 7, 32, 37, 661322, tzinfo=utc)),
        ),
    ]
