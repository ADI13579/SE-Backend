from django.db.models import fields
from rest_framework import serializers
from .models import Program,Department,Subject,Semester,BachelorSubject,MasterSubject

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = "__all__"

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"

class SemesterSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(many=True)
    program = ProgramSerializer()
    class Meta:
        model = Semester
        fields = "__all__"

# program/:programId
# program desc -> semesters -> subjects
class ProgramSemesterSerializer(serializers.ModelSerializer):
    prog_code = ProgramSerializer()
    sub_code = SubjectSerializer()
    class Meta:
        model = Semester
        fields = ("id", "year","part","sub_code","prog_code")

