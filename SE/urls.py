

from django.urls import path
from . import views
  
urlpatterns = [
    path('', views.ApiOverview.as_view(), name='home'),
    # path('programs/', views.programs.as_view(), name='programs'),
    path('levels', views.Levels.as_view(), name='Levels'),
    path('level/<str:levelCode>', views.OneLevel.as_view(), name='OneLevel'),
    path('programs', views.Programs.as_view(), name='Programs'),
    path('program/<str:progCode>', views.OneProgram.as_view(), name='OneProgram'),
    path('subjects', views.Subjects.as_view(), name = "Subjects"),
    path('subject/<str:subCode>', views.OneSubject.as_view(), name="OneSubject"),
    path('bulk/subject', views.ProgramsUpload.as_view(), name="ProgramsUpload"),
    path('bulk/syllabus', views.SyllabusUpload.as_view(), name="SyllabusUpload"),
    
      
]