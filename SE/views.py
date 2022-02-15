from json import loads
from tkinter import E
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from .models import BachelorSubject, Program, Semester
from .serializers import ProgramSerializer, ProgramSemesterSerializer
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
    # print(levelCode)
    if levelCode == "BE":
      # join program table with level code "BE" with semesters table and subject table
      results = Semester.objects.select_related('prog_code','sub_code').filter(prog_code__level_code__exact='BE').values("year","part","prog_code","sub_code","prog_code__prog_name","prog_code__description", "prog_code__dept_code")
      # results = Semester.objects.select_related('prog_code','sub_code').filter(prog_code__level_code__exact='BE').values("__all__" )

    elif levelCode=="MSC":
      # join master table with subject table:
      results = Semester.objects.select_related('prog_code','sub_code').filter(prog_code__level_code__exact='MSC').values("year","part","prog_code","sub_code","prog_code__prog_name","prog_code__description", "prog_code__dept_code")
      print(results)
    else:
      return utils.failure(
        "level fetch",
      "level fetched unsuccesfully",
      status.HTTP_404_NOT_FOUND
      )
    data = hf.format_get_levels(results,levelCode)
    print("meeee")
    return utils.success(
      "level fetch",
      "level fetched succesfully",
              data  
              )

  def put(self,request, levelCode):
    try:
      dataIn = request.POST
      programs = loads(dataIn["programs"])
      # Entry.objects.filter(pub_date__year=2005).delete()
      print(programs)
      Program.objects.filter(level_code=levelCode).exclude(prog_code__in=programs).delete()
      return utils.success(
          "level update",
          "level updated successfully",
        )

    except Exception as e:
        return utils.failure(
          "level update",
        str(e)
        )

class Programs(APIView):
  def post(self, request):
    try:
      # gets the json data
      inputData = request.data
      # print(request.data)
      # return Response()
      # changes, frontend : send json argument for levelcode and programcode
      level_code = inputData.get("levelCode")
      prog_code = inputData.get("progCode","RNDPROG")
      print(inputData)
      Program(prog_code=prog_code, level_code =level_code).save()
      return utils.success(
        "program creation",
        "program craeted succesfully",
        
      )
    except Exception as e:
        return utils.failure(
          "program creation",
        str(e)
        )

  def get(self, request):
    try:
      results = Program.objects.all().values("prog_code","prog_name")
      data = hf.format_get_programs(results)
      return utils.success(
        "program creation",
        "program craeted succesfully",
        data
        
      )
    except Exception as e:
        return utils.failure(
          "program creation",
        str(e)
        )

class OneProgram(APIView):
  def delete(self, request, progCode):
    try:

      Program(prog_code=progCode).delete()
      return utils.success(
        "program deletion",
        "program deleted succesfully",
        
      )
    except Exception as e:
        return utils.failure(
          "program deletion",
        str(e)
        )

  def get(self,request, progCode):
    try:
      results =   Semester.objects.select_related('prog_code','sub_code').filter(prog_code__exact=progCode).values("year","part","prog_code","sub_code","prog_code__prog_name","prog_code__description", "prog_code__dept_code", "sub_code__sub_name")
      data = hf.format_get_levels(results,"")["programs"][0]
      return utils.success(
        "program fetch",
        "program fetched succesfully",
        data
        
      )
    except Exception as e:
        return utils.failure(
          "program fetch",
        str(e)
        )


  def testget(self,request, progCode):
    try:
        data = Semester.objects.filter(prog_code=progCode)
        item = ProgramSemesterSerializer(data, many=True)
        return utils.success(
        "program fetch",
        "program fetched succesfully",
        item.data
        
        )
    except Exception as e:
        return utils.failure(
          "program fetch",
        str(e)
        )

      

  def put(self,request,progCode):
    return Response()





