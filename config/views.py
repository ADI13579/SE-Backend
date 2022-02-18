
from django.http import FileResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse

def download_file(request,filePath):
  try:
      return HttpResponse(open(f"syllabus/{filePath}", 'rb'))
  except Exception as e:
      print(str(e))
      return Response()
