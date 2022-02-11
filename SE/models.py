from django.db import models

# Create your models here.
class Program(models.Model):
    prog_code= models.CharField(primary_key=True,max_length=10, default=None)
    prog_name= models.CharField(max_length=50, default=None)
    def __str__(self):
        return self.code

class Department(models.Model):
    dept_code= models.CharField(primary_key=True,max_length=10, default=None)
    dept_name= models.CharField(max_length=50, default=None)
    prog_code = models.ForeignKey(Program, default=None, on_delete=models.CASCADE)
    def __str__(self):
        return self.code

class Subject(models.Model):
    sub_code= models.CharField(primary_key=True,max_length=10, default=None)
    level=models.CharField(max_length=10,blank=True)
    sub_name= models.CharField(max_length=100, default=None)
    elective=models.BooleanField(default=False)
    implemented_on = models.DateField(null=False)    
    dept_code = models.ForeignKey(Department, default=None, on_delete=models.CASCADE)
    def __str__(self):
        return self.code+'('+self.name+')'

class Semester(models.Model):
    year= models.PositiveSmallIntegerField(default=None)
    part= models.PositiveSmallIntegerField(default=None)
    dept_code=models.ForeignKey(Department,default=None,on_delete=models.CASCADE)

class BachelorSubject(models.Model):
    hours= models.PositiveSmallIntegerField(default=None)
    external_marks=models.PositiveSmallIntegerField(default=80)
    internal_marks=models.PositiveSmallIntegerField(default=20)
    practical_marks=models.PositiveSmallIntegerField(default=None)
    syllabus=models.FileField(upload_to='syllabus',blank=True)
    elective=models.BooleanField(default=False)
    subt_code = models.ForeignKey(Subject, default=None, on_delete=models.CASCADE)
    def __str__(self):
        return self.subject

class MasterSubject(models.Model):
    credit= models.PositiveSmallIntegerField(default=None)
    internal=models.PositiveSmallIntegerField(default=80)
    external=models.PositiveSmallIntegerField(default=20)
    syllabus=models.FileField(upload_to='syllabus',blank=True)
    practical_marks=models.PositiveSmallIntegerField(default=None)
    subt_code = models.ForeignKey(Subject, default=None, on_delete=models.CASCADE)
    def __str__(self):
        return self.subject