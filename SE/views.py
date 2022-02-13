from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from .models import Program
from .serializers import ProgramSerializer
from rest_framework.views import APIView

class ApiOverview(APIView):
    """
    List all Transformers, or create a new Transformer
    """
  
    def get(self, request):

        return Response({"happy":"coding"})
  








@api_view(['POST','GET'])
def programs(request):
    print(request.method)
    item = ProgramSerializer(data=request.data)

	# validating for already existing data
    if Program.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

