from pyexpat import model
from django.db import models
import uuid

# Create your models here.
# DOECE
class Department(models.Model):
    dept_code= models.CharField(primary_key=True,max_length=100, default=None)
    dept_name= models.CharField(max_length=100, default=None)
    def __str__(self):
        return self.dept_code
# BCT
class Program(models.Model):
    BACHELORS = 'BE'
    MASTERS = 'MSC'

    CHOICES_A = (
        (BACHELORS, BACHELORS),
        (MASTERS, MASTERS),
    )
    prog_code= models.CharField(primary_key=True,max_length=100, default=None)
    prog_name= models.CharField(max_length=100, default="default_name")
    dept_code=models.ForeignKey(Department,default="RND",on_delete=models.CASCADE,db_column="dept_code")
    description= models.CharField(max_length=500, blank = True, default = "description")
    level_code= models.CharField(max_length=100,choices=CHOICES_A ,default=None)



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
    class Meta:
        unique_together = (('year', 'part','prog_code'),)


    year= models.PositiveSmallIntegerField(default=None)
    part= models.PositiveSmallIntegerField(default=None)
    prog_code = models.ForeignKey(Program, default=None, on_delete=models.CASCADE,db_column="prog_code")
    sub_code = models.ForeignKey(Subject, default=None, on_delete=models.CASCADE,db_column="sub_code")
    def __str__(self):
        return str(self.year)+' '+str(self.part)+' '+str(self.prog_code)+' '+str(self.sub_code)

class BachelorSubject(models.Model):
    id = models.CharField(primary_key=True, default=uuid.uuid4, editable=False,max_length=200)
    hours= models.PositiveSmallIntegerField(null=True,blank=True)
    theory_marks=models.PositiveSmallIntegerField(default=80)
    practical_marks=models.PositiveSmallIntegerField(null=True,blank=True)
    syllabus=models.FileField(upload_to='syllabus',null=True,blank=True)
    sub_code = models.ForeignKey(Subject,null=True,blank=True, on_delete=models.CASCADE,db_column="sub_code")
    revised_on = models.DateTimeField(null=True,blank=True)    
    revised=models.BooleanField(default=False)
    elective=models.BooleanField(default=False)
    remarks=models.CharField(max_length=200,null=True,blank=True)
    def __str__(self):
        return self.sub_code.sub_name

class MasterSubject(models.Model):
    id = models.CharField(primary_key=True, default=uuid.uuid4, editable=False,max_length=200) 
    credit= models.PositiveSmallIntegerField(default=4)
    internal=models.PositiveSmallIntegerField(default=20)
    external=models.PositiveSmallIntegerField(default=80)
    syllabus=models.FileField(upload_to='syllabus',null=True,blank=True)
    sub_code = models.ForeignKey(Subject, null=True,blank=True, on_delete=models.CASCADE,db_column="sub_code")
    revised=models.BooleanField(default=False)
    revised_on = models.DateField(null=True,blank=True)    
    remarks=models.CharField(max_length=200,null=True,blank=True)
    def __str__(self):
        return self.sub_code.sub_name+"("+self.sub_code+"):"+self.revised_on
