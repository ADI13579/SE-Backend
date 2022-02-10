import uuid
from sqlite3 import Date
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone

class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.dob = timezone.now()
        user.set_password(password)
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save()

        return user

class UserAccount(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    image = models.ImageField(null=True)
    
    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.first_name+" "+self.last_name

class Program(models.Model):
    code= models.CharField(primary_key=True,max_length=10, default=None)
    name= models.CharField(max_length=50, default=None)
    def __str__(self):
        return self.code

class Department(models.Model):
    code= models.CharField(primary_key=True,max_length=10, default=None)
    name= models.CharField(max_length=50, default=None)
    program = models.ForeignKey(Program, default=None, on_delete=models.CASCADE)
    def __str__(self):
        return self.code+'('+self.name+')'

class Subject(models.Model):
    code= models.CharField(primary_key=True,max_length=10, default=None)
    level=models.CharField(max_length=10,blank=True)
    name= models.CharField(max_length=100, default=None)
    elective=models.BooleanField(default=False)
    implemented_on = models.DateField(null=False)    
    department = models.ForeignKey(Department, default=None, on_delete=models.CASCADE)
    def __str__(self):
        return self.code+'('+self.name+')'

class Semester(models.Model):
    year= models.PositiveSmallIntegerField(default=None)
    part= models.PositiveSmallIntegerField(default=None)
    department=models.ForeignKey(Department,default=None,on_delete=models.CASCADE)

class BachelorSubject(models.Model):
    hours= models.PositiveSmallIntegerField(default=None)
    external_marks=models.PositiveSmallIntegerField(default=80)
    internal_marks=models.PositiveSmallIntegerField(default=20)
    practical_marks=models.PositiveSmallIntegerField(default=None)
    syllabus=models.FileField(upload_to='syllabus',blank=True)
    elective=models.BooleanField(default=False)
    subject = models.ForeignKey(Subject, default=None, on_delete=models.CASCADE)
    def __str__(self):
        return self.subject

class MasterSubject(models.Model):
    credit= models.PositiveSmallIntegerField(default=None)
    internal=models.PositiveSmallIntegerField(default=80)
    external=models.PositiveSmallIntegerField(default=20)
    syllabus=models.FileField(upload_to='syllabus',blank=True)
    practical_marks=models.PositiveSmallIntegerField(default=None)
    subject = models.ForeignKey(Subject, default=None, on_delete=models.CASCADE)
    def __str__(self):
        return self.subject