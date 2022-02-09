from rest_framework import generics,permissions
from .models import UserAccount
# from .serializers import GetCourseSerializer,CreateCourseSerializer,CompleteCourseSerializer,UpdateCourseSerializer,CreateLessonSerializer,CompleteLessonSerializer,UpdateLessonSerializer,CommentSerializer,BasicUserSerializer
from .serializers import  BasicUserSerializer
# from .permissions import CourseModify,LessonModify

class GetUserInfo(generics.ListAPIView):
    permissions_classes=(permissions.IsAuthenticated,)
    queryset=UserAccount.objects.all()
    serializer_class=BasicUserSerializer

# class GetCourse(generics.ListAPIView):
#     permission_classes = (permissions.IsAuthenticated,)
#     queryset = Courses.objects.all()
#     serializer_class = GetCourseSerializer

# class CreateCourse(generics.CreateAPIView):
#     permission_classes = (permissions.IsAuthenticated,CourseModify,)
#     queryset=Courses.objects.none()
#     serializer_class = CreateCourseSerializer

# class CompleteCourseDetail(generics.ListAPIView):
#     permission_classes = (permissions.IsAuthenticated,)
#     queryset = Courses.objects.all()
#     serializer_class = CompleteCourseSerializer

# class UpdateCourse(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (permissions.IsAuthenticated,CourseModify,)
#     queryset =Courses.objects.all();
#     serializer_class = UpdateCourseSerializer

# class CreateLesson(generics.CreateAPIView):
#     permission_classes = (permissions.IsAuthenticated,LessonModify,)
#     serializer_class = CreateLessonSerializer

# class UpdateLesson(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (permissions.IsAuthenticated,LessonModify,)
#     queryset = Lesson.objects.all()
#     serializer_class = UpdateLessonSerializer

# class CompleteLessonDetail(generics.ListAPIView):
#     permission_classes = (permissions.IsAuthenticated,)
#     queryset = Lesson.objects.all()
#     serializer_class = CompleteLessonSerializer

# class CommentHandle(generics.ListCreateAPIView):
#     permission_classes = (permissions.IsAuthenticated,)
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
