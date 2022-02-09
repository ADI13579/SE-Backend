from django.contrib import admin
from .models import  UserAccount
# Register your models here.
from .models import Program,Department,Subject,BachelorSubject,MasterSubject,Semester

admin.site.register(UserAccount)
admin.site.register(Program)
admin.site.register(Department)
admin.site.register(Subject)

admin.site.register(BachelorSubject)
admin.site.register(MasterSubject)
admin.site.register(Semester)