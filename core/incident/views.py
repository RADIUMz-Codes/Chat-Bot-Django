from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from incident.serializers import IncidentSerializer, IncidentTypeSerializer
from incident.models import Incident, IncidentTypes

@api_view(["GET", "POST"])
def incident(request):
    if request.method == "GET":
        objs = Incident.objects.all()
        serializer = IncidentSerializer(objs, many = True)
        if len(serializer.data) == 0:
            return Response({
                'message' : 'No Incidents Yet'
            }, status= status.HTTP_204_NO_CONTENT)
        return Response(serializer.data, status= status.HTTP_200_OK)
    elif request.method == "POST":
        data = request.data
        serializer = IncidentSerializer(data= data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        
@api_view(['GET'])
def incident_types(request):
    if request.method == 'GET':
        objs = IncidentTypes.objects.all()
        serializer = IncidentTypeSerializer(objs, many = True)
        return Response(serializer.data, status= status.HTTP_200_OK)