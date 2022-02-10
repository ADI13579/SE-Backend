from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model


User = get_user_model()

class BasicUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'username','email','image')

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id','username', 'email', 'password', 'image')

# class GetCourseSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = ('id', 'instructor', 'title','thumbnail')
#         model = Courses

# class CreateCourseSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = ('id', 'instructor', 'title', 'description', 'duration', 'thumbnail')
#         model = Courses


# class UpdateCourseSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = ('title', 'description', 'duration', 'thumbnail')
#         model = Courses

# class AbstractLessonSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = ('id','title','date_uploaded')
#         model = Lesson

# class CompleteCourseSerializer(serializers.ModelSerializer):
#     lessons = AbstractLessonSerializer(many=True)
#     class Meta:
#         fields = ('id', 'instructor', 'title', 'description', 'duration', 'thumbnail','lessons','user')
#         model = Courses

# class CreateLessonSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = ('id', 'instructor', 'title', 'description', 'video','date_uploaded','material','course')
#         model = Lesson

# class UpdateLessonSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = ('title', 'description', 'video', 'date_uploaded','material')
#         model = Lesson

# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields=('user','lesson','description')
#         model=Comment

# class CompleteLessonSerializer(serializers.ModelSerializer):
#     comments=CommentSerializer(many=True)
#     class Meta:
#         fields = ('id', 'instructor', 'title', 'description', 'video','date_uploaded','material','course','comments')
#         model = Lesson