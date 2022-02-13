

from django.urls import path
from . import views
  
urlpatterns = [
    path('', views.ApiOverview.as_view(), name='home'),
    # path('programs/', views.programs.as_view(), name='programs'),
      
]