# Generated by Django 4.0.1 on 2022-01-22 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ocw', '0020_rename_instructor_comments_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='ocw.lesson'),
        ),
    ]
