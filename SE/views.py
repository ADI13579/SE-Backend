from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from .models import BachelorSubject, Program, Semester
from .serializers import ProgramSerializer
from rest_framework.views import APIView
from . import helper_functions as hf 
from . import response_utils as utils 

class ApiOverview(APIView):
    """
    List all Transformers, or create a new Transformer
    """
  
    def get(self, request):

        return Response({"happy":"coding"})
  



class Levels(APIView):

	def get(self, request):
		# acc to ER diagram the levels cant be made dynamic, since they have thier own table
		result = {"data": [
    {
      "_id": {
        "$oid": "1"
      },
      "code": "BE",
      "name": "Bachelor in Engineering ",
      "image": "sample.jpg"
    },
    {
      "_id": {
        "$oid": "2"
      },
      "code": "MSC",
      "name": "Masters in Engineering",
      "image": "sample.jpg"
    }
  ]
	}

		return Response(result)
  

class OneLevel(APIView):

  def get(self, request, levelCode):
		# acc to ER diagram the levels cant be made dynamic, since they have thier own table
    result = None 
    print(levelCode)
    if levelCode == "BE":
      # join program table with level code "BE" with semesters table and subject table
      results = Semester.objects.select_related('prog_code','sub_code').filter(prog_code__level_code__exact='BE').values("year","part","prog_code","sub_code","prog_code__prog_name","prog_code__description", "prog_code__dept_code")
      
    elif levelCode=="MSC":
      # join master table with subject table:
      results = Semester.objects.select_related('prog_code','sub_code').filter(prog_code__level_code__exact='MSC').values()
      # print(results)
    else:
      return utils.failure(
        "level fetch",
      "level fetched unsuccesfully",
      status.HTTP_404_NOT_FOUND
      )
    data = hf.format_get_levels(results,levelCode)

    return utils.success(
      "level fetch",
      "level fetched succesfully",
              data  
              )
  





