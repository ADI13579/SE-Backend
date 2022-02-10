from django.urls import path
# from .views import GetCourse,CreateCourse,UpdateCourse, CompleteCourseDetail,CreateLesson,UpdateLesson,CommentHandle,CompleteLessonDetail,GetUserInfo
from .views import GetUserInfo,UserAccount
urlpatterns = [
    path('user/',GetUserInfo.as_view()),
]