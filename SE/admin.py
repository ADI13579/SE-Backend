from django.contrib import admin
from .models import Program,Department,Subject,BachelorSubject,MasterSubject,Semester
# Register your models here.

admin.site.register(Program)
admin.site.register(Department)
admin.site.register(Subject)

admin.site.register(BachelorSubject)
admin.site.register(MasterSubject)
admin.site.register(Semester)
