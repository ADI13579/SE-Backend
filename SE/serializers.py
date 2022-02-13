from django.db.models import fields
from rest_framework import serializers
from .models import Program,Department,Subject,Semester,BachelorSubject,MasterSubject

class ProgramSerializer(serializers.ModelSerializer):
	class Meta:
		model = Program
		fields = ('prog_code', 'prog_name')


