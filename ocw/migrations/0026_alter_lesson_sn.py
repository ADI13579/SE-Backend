# Generated by Django 4.0.1 on 2022-01-22 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocw', '0025_alter_lesson_sn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='sn',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
