from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Location
from .serializers import LocationSerializer

# Create your views here.
@api_view(['GET'])
def locationsList(request):
    locations = Location.objects.all()
    serializer = LocationSerializer(locations, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def locationDetails(request, pk):
    try:
        location = Location.objects.get(id=pk)
        serializer = LocationSerializer(location, many=False)
    
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response("Location with that ID not found", status=status.HTTP_404_NOT_FOUND)