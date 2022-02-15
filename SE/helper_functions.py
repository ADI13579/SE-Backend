{"programs": [
      {
        "_id": {
          "$oid": "611a1adb89394f141864c096"
        },
        "code": "BCT",
        "name": "Bachelor of computer Engineering(updated)",
        "image": "c3f28ccf-e151-4f82-b381-67f417a53e3e.jpg",
        "description": "Bachelor of computer Engineering IOE BCT Syllabus, New Course which is Updated Syllabus (2066), Course Contents for Institute of Engineering (IOE) including affiliated Engineering Colleges / Academic Institutions affiliated to Tribhuvan University (TU), Nepal.",
        "semesters": {
          "1": {
            "subjects": [
              "SH401",
              "CT401",
              "AS501"
            ]
          },
          "2": {
            "subjects": [
              "SH451",
              "UH451"
            ]
          },
          "3": {
            "subjects": [
              "SH451"
            ]
          },
          "4": {
            "subjects": [
              "SH401"
            ]
          },
          "5": {
            "subjects": [
              "SH553"
            ]
          },
          "6": {
            "subjects": [
              "CE655"
            ]
          }
        },
        "level": "BE",
      },

      {
        "_id": {
          "$oid": "6208d1dea5156e2d6f80399c"
        },
        "code": "CODE",
        "name": "sampleName",
        "level": "BE",
        "image": "sample.jpg",
        "description": "Description",
        "semesters": {
          "1": {
            "subjects": []
          },
          "2": {
            "subjects": []
          }
        }
      }
    ]
}
def format_get_levels(results, levelCode=None ):
    res = {
    "_id": {
      "$oid": "1"
    },
    "code": levelCode,
    "name": "Bachelor in Engineering " if levelCode =="BE" else "Masters in Engineering",
    "programs":[],
    "image": "sample.jpg"
  }
    # print(results)
    programs_code =set()
    programs_detail={}
    for result in results:
      # traverse for department
      if result["prog_code"] not in programs_code:
        programs_code.add(result["prog_code"])
        program_dict = {
              "_id": {
                "$oid": result["prog_code"]
              },
              "code":result["prog_code"],
              "name": result["prog_code__prog_name"],
              "image": "sample.jpg",
              "description": result["prog_code__description"],
              "semesters":{}
              }
        programs_detail[result["prog_code"]] =program_dict

    # res["programs"] =list(programs)
    for result in results:
      # traverse for semesters and subjects :
      semester = result["year"] *2 - result["part"] %2
      # programs_detail[result["prog_code"]]["semesters"][semester]= programs_detail[result["prog_code"]]["semesters"].get(semester,{"subjects":[]})["subjects"].append(result["sub_code"]) #{"subjects":[]}
      # programs_detail[result["prog_code"]]["semesters"][semester]= programs_detail[result["prog_code"]]["semesters"].get(semester,{"subjects":[]})["subjects"].append(result["sub_code"]) #{"subjects":[]}
      programs_detail[result["prog_code"]]["semesters"][semester] = programs_detail[result["prog_code"]]["semesters"].get(semester,{"subjects":[]})
      if  levelCode:
        programs_detail[result["prog_code"]]["semesters"][semester]["subjects"].append(result["sub_code"])
      else:
        '''{
            "_id": {
              "$oid": "611a186499d67e88b3fac1cd"
            },
            "code": "SH401",
            "level": "BE",
            "name": "Maths",
            "filename": "f3323144-db4a-460b-bd29-8108a72459e1.pdf"
          },'''
        programs_detail[result["prog_code"]]["semesters"][semester]["subjects"].append(
          {
            "_id": {
              "$oid": result["sub_code"]
            },
            "code": result["sub_code"],
            "name": result["sub_code__sub_name"],

          }
        )


    # x = (programs_detail.values())
    res["programs"].extend(programs_detail.values())
    return res


def format_get_programs(results):
  '''
      {"_id": {
        "$oid": "611a1abe89394f141864c095"
      },
      "code": "BCE",
      "name": "Bachelor in civil engineering",
          }'''
  return [
    {"_id": {
        "$oid": result["prog_code"]
      },
      "code": result["prog_code"],
      "name": result["prog_name"],
          }
          for result in results

  ]



