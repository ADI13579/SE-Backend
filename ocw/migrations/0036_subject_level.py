# Generated by Django 4.0.1 on 2022-02-09 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocw', '0035_bachelorsubject_department_mastersubject_program_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='level',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]