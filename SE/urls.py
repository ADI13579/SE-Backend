

from django.urls import path
from . import views
  
urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('programs/', views.programs, name='programs'),
      
]