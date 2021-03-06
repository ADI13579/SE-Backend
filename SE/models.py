from pyexpat import model
from django.db import models

# Create your models here.
# DOECE
class Department(models.Model):
    dept_code= models.CharField(primary_key=True,max_length=100, default=None)
    dept_name= models.CharField(max_length=100, default=None)
    def __str__(self):
        return self.dept_code
# BCT
class Program(models.Model):
    prog_code= models.CharField(primary_key=True,max_length=100, default=None)
    prog_name= models.CharField(max_length=100, default=None)
    dept_code=models.ForeignKey(Department,default=None,on_delete=models.CASCADE,db_column="dept_code")
    def __str__(self):
        return self.prog_code

class Subject(models.Model):
    sub_code= models.CharField(primary_key=True,max_length=100, default=None)
    level=models.CharField(max_length=100,blank=True)
    sub_name= models.CharField(max_length=100, default=None)
    elective=models.BooleanField(default=False)
    implemented_on = models.DateField(null=False)    
    prog_code = models.ForeignKey(Program, default=None, on_delete=models.CASCADE,db_column="prog_code")
    def __str__(self):
        return self.sub_code+'('+self.sub_name+')'

class Semester(models.Model):
    year= models.PositiveSmallIntegerField(default=None)
    part= models.PositiveSmallIntegerField(default=None)
    prog_code = models.ForeignKey(Program, default=None, on_delete=models.CASCADE,db_column="prog_code")
    sub_code = models.ForeignKey(Subject, default=None, on_delete=models.CASCADE,db_column="sub_code")
    def __str__(self):
        return str(self.year)+' '+str(self.part)+' '+str(self.prog_code)+' '+str(self.sub_code)

class BachelorSubject(models.Model):
    hours= models.PositiveSmallIntegerField(default=None)
    external_marks=models.PositiveSmallIntegerField(default=80)
    internal_marks=models.PositiveSmallIntegerField(default=20)
    practical_marks=models.PositiveSmallIntegerField(default=None)
    syllabus=models.FileField(upload_to='syllabus',blank=True)
    elective=models.BooleanField(default=False)
    sub_code = models.ForeignKey(Subject, default=None, on_delete=models.CASCADE,db_column="sub_code")
    def __str__(self):
        return self.sub_code.sub_name

class MasterSubject(models.Model):
    credit= models.PositiveSmallIntegerField(default=4)
    internal=models.PositiveSmallIntegerField(default=20)
    external=models.PositiveSmallIntegerField(default=80)
    syllabus=models.FileField(upload_to='syllabus',blank=True)
    sub_code = models.ForeignKey(Subject, default=None, on_delete=models.CASCADE,db_column="sub_code")
    def __str__(self):
        return self.sub_code.sub_name