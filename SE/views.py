from json import loads
from sys import implementation
from tkinter import E
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from .models import BachelorSubject, Program, Semester, Subject, MasterSubject, Department
from .serializers import ProgramSerializer, ProgramSemesterSerializer
from rest_framework.views import APIView
from . import helper_functions as hf
from . import response_utils as utils
from django.http import FileResponse
import pandas as pd
from collections import defaultdict
import datetime


class ApiOverview(APIView):
    """
    List all Transformers, or create a new Transformer
    """

    def get(self, request):

        return Response({"happy": "coding"})


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
            results = Semester.objects.select_related('prog_code', 'sub_code').filter(prog_code__level_code__exact='BE').values(
                "year", "part", "prog_code", "sub_code", "prog_code__prog_name", "prog_code__description", "prog_code__dept_code")
            # results = Semester.objects.select_related('prog_code','sub_code').filter(prog_code__level_code__exact='BE').values("__all__" )

        elif levelCode == "MSC":
            # join master table with subject table:
            results = Semester.objects.select_related('prog_code', 'sub_code').filter(prog_code__level_code__exact='MSC').values(
                "year", "part", "prog_code", "sub_code", "prog_code__prog_name", "prog_code__description", "prog_code__dept_code")
            print(results)
        else:
            return utils.failure(
                "level fetch",
                "level fetched unsuccesfully",
                status.HTTP_404_NOT_FOUND
            )
        data = hf.format_get_levels(results, levelCode)
        return utils.success(
            "level fetch",
            "level fetched succesfully",
            data
        )

    def put(self, request, levelCode):
        try:
            dataIn = request.POST
            programs = loads(dataIn["programs"])
            # Entry.objects.filter(pub_date__year=2005).delete()
            print(programs)
            Program.objects.filter(level_code=levelCode).exclude(
                prog_code__in=programs).delete()
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
            prog_code = inputData.get("progCode", "RNDPROG")
            print(inputData)
            Program(prog_code=prog_code, level_code=level_code).save()
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
            results = Program.objects.all().values("prog_code", "prog_name")
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

    def get(self, request, progCode):
        try:
            results = Semester.objects.select_related('prog_code', 'sub_code').filter(prog_code__exact=progCode).values(
                "year", "part", "prog_code", "sub_code", "prog_code__prog_name", "prog_code__description", "prog_code__dept_code", "sub_code__sub_name")
            data = hf.format_get_levels(results, "")["programs"][0]
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

    def testget(self, request, progCode):
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

    def put(self, request, progCode):
        return Response()


class Subjects(APIView):
    def get(self, request):
        try:
            var = Subject.objects.distinct().values(
                'sub_code', 'sub_name', 'prog_code__level_code')
            data = []
            for i in var:
                if(i['prog_code__level_code'] == "BE"):
                    dict = {
                        "_id": {
                            "$oid": i['sub_code']
                        },
                        "code": i['sub_code'],
                        "name": i['sub_name']
                    }
                    data.append(dict)
                elif(i['prog_code__level_code'] == "MSC"):
                    dict = {
                        "_id": {
                            "$oid": i['sub_code']
                        },
                        "code": i['sub_code'],
                        "name": i['sub_name']
                    }

                    data.append(dict)

            return utils.success(
                "subjects fetch",
                "subjects fetched succesfully",
                data
            )
        except Exception as e:
            return utils.failure(
                "subjects fetch",
                str(e)
            )

    def post(self, request):
        # try:
            dataIn = request.data
            print(dataIn)
            program = Program.objects.filter(prog_code=dataIn["progCode"])
            subject = Subject(
                sub_code=dataIn["subCode"],
                sub_name=dataIn["subName"],
                prog_code=program[0],
                implemented_on=datetime.date.today()
            )
            subject.save()

            return utils.success(
                "One subject addition",
                "One subject added succesfully",

            )
        # except Exception as e:
        #     return utils.failure(
        #         "One subject addition",
        #         str(e)
        #     )


class OneSubject(APIView):
    def get(self, request, subCode):
        try:
            assert len(Subject.objects.all().filter(
                sub_code=subCode).distinct()), f"No such subject exist"
            query = Subject.objects.all().filter(sub_code=subCode).distinct().values(
                'sub_name', 'prog_code','prog_code__level_code')
            data = {
                "_id": {
                    "$oid": subCode
                },
                "code": subCode,
                "name": query[0]['sub_name'],
                "progCode": query[0]['prog_code'],
                "level": query[0]['prog_code__level_code'],
            }
            syllabus = []
            if(len(BachelorSubject.objects.all().filter(sub_code=subCode))):
                query = BachelorSubject.objects.all().filter(sub_code=subCode).values('id', 'theory_marks',
                                                                                      'practical_marks', 'hours', 'revised_on', 'remarks', 'syllabus', 'revised')
                for i in query:
                    temp = {
                        "id": i['id'],
                        "theory": i['theory_marks'],
                        "practical": i['practical_marks'],
                        "teaching": i['hours'],
                        "batch": str(i['revised_on'])[:4],
                        "remarks": i['remarks'],
                        "filename": i['syllabus'],
                        "revised": i['revised']
                    }
                    syllabus.append(temp)
            elif(len(MasterSubject.objects.all().filter(sub_code=subCode))):
                query = MasterSubject.objects.all().filter(sub_code=subCode).values(
                    'id', 'credit', 'internal', 'external', 'revised_on', 'remarks', 'syllabus', 'revised')
                syllabus = []
                for i in query:
                    temp = {
                        'id': i['id'],
                        "credit": i['credit'],
                        "internal": i['internal'],
                        "external": i['external'],
                        "batch": str(i['revised_on'])[:4],
                        "remarks": i['remarks'],
                        "filename": i['syllabus'],
                        "revised": i['revised']
                    }
                    syllabus.append(temp)
            else:
                assert f"subject not found"
            data['syllabus'] = syllabus
            return utils.success(
                "One subject fetch",
                "One subject fetched succesfully",
                data
            )
        except Exception as e:
            return utils.failure(
                "One subject fetch",
                str(e)
            )

    def put(self, request, subCode):
        # try:
            data = request.POST  # store the json request body in data
            file = request.FILES.get("file")

            prog = Program.objects.filter(prog_code=data['progCode'])
            if(not len(prog)):
                assert "Program Doesn't Exist"
            level = prog.values()[0]['level_code']
            # if the sub_code doesnt exist create a new subject
            if(not len(Subject.objects.filter(sub_code=subCode))):
                assert "subject doesn't exist"
            

            sub = Subject.objects.get(sub_code=subCode)
            # sub.sub_code=data['subCode']
            sub.sub_name = data['name']
            print(sub.sub_name )
            sub.level = level
            sub.prog_code = prog[0]
            # sub.implemented_on=datetime.date(int(data['batch']),1,1)
            sub.save()
            # If found the old_batch and old_code then any of it can be renamed else a new object is created
            if(level == "BE"):

                bach = BachelorSubject()
                if(len(BachelorSubject.objects.filter(sub_code=subCode))):
                    if(data.get("batch") and len(BachelorSubject.objects.filter(sub_code=subCode, revised_on=datetime.date(int(data['batch']), 1, 1)))):
                        bach = BachelorSubject.objects.filter(
                            sub_code=subCode, revised_on=datetime.date(int(data['batch']), 1, 1))[0]

                # bach.sub_code=Subject.objects.all().filter(sub_code=subCode)[0]
                bach.sub_code = sub
                if file:
                  bach.syllabus=file
                bach.theory_marks = data['theory']
                bach.practical_marks = data['practical']
                bach.hours = data['teaching']
                bach.revised_on = datetime.date(int(data.get('batch',datetime.date.today().year)), 1, 1)
                bach.remarks = data['remarks']
                if(len(BachelorSubject.objects.all().filter(sub_code=bach.sub_code))):
                    bach.revised = True
                bach.save()
                response_data = str(bach.id)
            elif(level == "MSC"):
                mas = MasterSubject()
                if(len(MasterSubject.objects.filter(sub_code=subCode))):
                    if(data.get('batch') and len(MasterSubject.objects.filter(sub_code=subCode, revised_on=datetime.date(int(data['batch']), 1, 1)))):
                        mas = MasterSubject.objects.get(
                            sub_code=subCode, revised_on=datetime.date(int(data['batch']), 1, 1))


                # credit=>has default 4
                mas.internal = data['theory']
                mas.external = data['practical']
                # we need to upload a file here 
                if file:
                  mas.syllabus=file
                mas.sub_code = sub
                mas.revised_on = datetime.date(int(data.get('batch',datetime.date.today().year)), 1, 1)
                mas.remarks = data['remarks']
                if(len(MasterSubject.objects.all().filter(sub_code=mas.sub_code))):
                    mas.revised = True
                mas.save()
                response_data = str(mas.id)
            else:
                assert f"No valid level to add the subject"

            return utils.success(
                "Subject Update",
                "Subject Updated Succesfully",
                {"id": response_data}

            )
        # except Exception as e:
        #     return utils.failure(
        #         "Subject Update",
        #         str(e)
        #     )


# class ProgramsUpload(APIView):
#     def post(self, request):
#         try:

#             data = request.FILES['file']
#             df = pd.read_csv(data)
#             df["implemented"] = pd.to_datetime(df["implemented"])
#             dept_codes = defaultdict(str)
#             prog_codes = defaultdict(str)
#             sub_codes = defaultdict(str)

#             for i, row in df.iterrows():
#                 try:
#                     dept_code = dept_codes[row["dept_code"].upper()]
#                     if dept_code == "":
#                         dept_codes[row["dept_code"].upper()] = Department.objects.get(
#                             dept_code=row["dept_code"].upper())
#                 except Department.DoesNotExist:
#                     dept_codes[row["dept_code"].upper()] = Department.objects.create(
#                         dept_code=row["dept_code"].upper(), dept_name=row["dept_name"])

#                 try:
#                     prog_code = prog_codes[row["prog_code"].upper()]
#                     if prog_code == "":
#                         prog_codes[row["prog_code"].upper()] = Program.objects.get(
#                             prog_code=row["prog_code"].upper())
#                 except Program.DoesNotExist:
#                     prog_codes[row["prog_code"].upper()] = Program.objects.create(prog_code=row["prog_code"].upper(), prog_name=row["prog_name"],
#                                                                                   level_code=row["level"], dept_code=dept_codes[row["dept_code"].upper()], description=row["description"])

#                 try:
#                     sub_code = sub_codes[row["sub_code"].upper()]
#                     if sub_code == "":
#                         sub_codes[row["sub_code"].upper()] = Subject.objects.get(
#                             sub_code=row["sub_code"].upper())
#                 except Subject.DoesNotExist:
#                     sub_codes[row["sub_code"].upper()] = Subject.objects.create(sub_code=row["sub_code"].upper(), sub_name=row["sub_name"], level=row["level"],
#                                                                                 prog_code=prog_codes[row["prog_code"].upper()], elective=row["elective"], implemented_on=row["implemented"])

#                 _ = Semester.objects.get_or_create(year=row["year"], part=row["part"], sub_code=sub_codes[row["sub_code"].upper(
#                 )], prog_code=prog_codes[row["prog_code"].upper()])

#             return utils.success(
#                 "Bulk upload subject ",
#                 "Bulk uploaded subject succesfully",

#             )
#         except Exception as e:
#             return utils.failure(
#                 "Bulk upload subject",
#                 str(e)
#             )


class BulkProgramsUpload(APIView):
    def post(self, request):
        data = request.FILES['csv_file']
        df = pd.read_csv(data)
        df["implemented"] = pd.to_datetime(df["implemented"])
        dept_codes = defaultdict(str)
        prog_codes = defaultdict(str)
        sub_codes = defaultdict(str)

        for i, row in df.iterrows():
            try:
                dept_code = dept_codes[row["dept_code"].upper()]
                if dept_code=="":
                    dept_codes[row["dept_code"].upper()] = Department.objects.get(dept_code=row["dept_code"].upper())
            except Department.DoesNotExist:
                dept_codes[row["dept_code"].upper()] = Department.objects.create(dept_code=row["dept_code"].upper(), dept_name=row["dept_name"])
            
            try:
                prog_code = prog_codes[row["prog_code"].upper()]
                if prog_code=="":
                    prog_codes[row["prog_code"].upper()] = Program.objects.get(prog_code=row["prog_code"].upper())
            except Program.DoesNotExist:
                prog_codes[row["prog_code"].upper()] = Program.objects.create(prog_code=row["prog_code"].upper(), prog_name=row["prog_name"], \
                    level_code=row["level"], dept_code=dept_codes[row["dept_code"].upper()], description=row["description"])

            try:
                sub_code = sub_codes[row["sub_code"].upper()]
                if sub_code=="":
                    sub_codes[row["sub_code"].upper()] = Subject.objects.get(sub_code=row["sub_code"].upper())
            except Subject.DoesNotExist:
                sub_codes[row["sub_code"].upper()] = Subject.objects.create(sub_code=row["sub_code"].upper(), sub_name=row["sub_name"], level=row["level"], \
                    prog_code=prog_codes[row["prog_code"].upper()], elective=row["elective"], implemented_on=row["implemented"])            

            try:
                _ = Semester.objects.get_or_create(year=row["year"], part=row["part"], sub_code=sub_codes[row["sub_code"].upper()], prog_code=prog_codes[row["prog_code"].upper()])
            except:
                print("Error in creating semester")

        return Response({})



class BulkSyllabusUpload(APIView):
    def post(self,request):
        data = request.FILES['csv_file']
        df = pd.read_csv(data)
        images = request.FILES.getlist('syllabus')
        files = {}
        if len(images) != df.shape[0]:
            return Response("Number of images and subjects do not match")
        
        for i,file in enumerate(images):
            files[file.name] = i

        sub_codes = defaultdict(str)

        for i, row in df.iterrows():
            try:
                sub_code = sub_codes[row["sub_code"].upper()]
                if sub_code=="":
                    sub_codes[row["sub_code"].upper()] = Subject.objects.get(sub_code=row["sub_code"].upper())
            except Subject.DoesNotExist:
                print(f"Subject doesn't exist for the {i+1}th row. Unable to add the syllabus")
                
            
            if True or request.POST.get('level')=="BE":
                # try:
                _ = BachelorSubject.objects.create(hours=row["hours"], theory_marks=row["theory"], practical_marks=row["practical"], \
                        sub_code=sub_codes[row["sub_code"].upper()], syllabus=images[files[row["syllabus"]]])
                # except:
                    # print("Error in creating Bachelor subject")
            elif request.POST.get('level')=="Msc":
                try:
                    _ = MasterSubject.objects.create(hours=row["hours"], external=row["external"], internal=row["internal"], \
                        sub_code=sub_codes[row["sub_code"].upper()], \
                        syllabus=images[files[row["syllabus"]]], elective=row["elective"])
                except:
                    print("Error in creating Master subject")

        return Response({})