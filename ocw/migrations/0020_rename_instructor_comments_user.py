# Generated by Django 4.0.1 on 2022-01-22 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ocw', '0019_comments_delete_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='instructor',
            new_name='user',
        ),
    ]
