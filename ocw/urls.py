from django.urls import path
# from .views import GetCourse,CreateCourse,UpdateCourse, CompleteCourseDetail,CreateLesson,UpdateLesson,CommentHandle,CompleteLessonDetail,GetUserInfo
from .views import GetUserInfo
urlpatterns = [
    path('user/<str:pk>',GetUserInfo.as_view()),
]