# Generated by Django 4.0.1 on 2022-01-22 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocw', '0012_remove_courses_thumbnail_image_path_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='date_joined',
            field=models.DateField(auto_now_add=True),
        ),
    ]