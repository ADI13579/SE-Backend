from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status

def success(operation,msg, data=None, status = status.HTTP_200_OK):
    # return Response()
    return Response(
        {"operation":operation,
        "success":True,
        "message":msg,
        "data":data

        },status=status
        )

def failure(operation, msg, status=status.HTTP_500_INTERNAL_SERVER_ERROR):
    return Response(
        {"operation":operation,
        "success":False,
        "message":msg,

        },status=status
        )