

from django.urls import path
from . import views
  
urlpatterns = [
    path('', views.ApiOverview.as_view(), name='home'),
    # path('programs/', views.programs.as_view(), name='programs'),
    path('levels', views.Levels.as_view(), name='levels'),
    path('level/<str:levelCode>', views.OneLevel.as_view(), name='OneLevel'),
    path('programs', views.Programs.as_view(), name='Programs'),
    path('program/<str:progCode>', views.OneProgram.as_view(), name='OneProgram'),
      
]