# Generated by Django 4.0.2 on 2022-02-11 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_code', models.CharField(default=None, max_length=10, primary_key=True, serialize=False)),
                ('dept_name', models.CharField(default=None, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('prog_code', models.CharField(default=None, max_length=10, primary_key=True, serialize=False)),
                ('prog_name', models.CharField(default=None, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('sub_code', models.CharField(default=None, max_length=10, primary_key=True, serialize=False)),
                ('level', models.CharField(blank=True, max_length=10)),
                ('sub_name', models.CharField(default=None, max_length=100)),
                ('elective', models.BooleanField(default=False)),
                ('implemented_on', models.DateField()),
                ('dept_code', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='SE.department')),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveSmallIntegerField(default=None)),
                ('part', models.PositiveSmallIntegerField(default=None)),
                ('dept_code', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='SE.department')),
            ],
        ),
        migrations.CreateModel(
            name='MasterSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit', models.PositiveSmallIntegerField(default=None)),
                ('internal', models.PositiveSmallIntegerField(default=80)),
                ('external', models.PositiveSmallIntegerField(default=20)),
                ('syllabus', models.FileField(blank=True, upload_to='syllabus')),
                ('practical_marks', models.PositiveSmallIntegerField(default=None)),
                ('subt_code', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='SE.subject')),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='prog_code',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='SE.program'),
        ),
        migrations.CreateModel(
            name='BachelorSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours', models.PositiveSmallIntegerField(default=None)),
                ('external_marks', models.PositiveSmallIntegerField(default=80)),
                ('internal_marks', models.PositiveSmallIntegerField(default=20)),
                ('practical_marks', models.PositiveSmallIntegerField(default=None)),
                ('syllabus', models.FileField(blank=True, upload_to='syllabus')),
                ('elective', models.BooleanField(default=False)),
                ('subt_code', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='SE.subject')),
            ],
        ),
    ]