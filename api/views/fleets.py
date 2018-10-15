from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from api.models.fleets import Fleet
from api.serializers.fleets import FleetSerializer
	
# Create your views here.

class FleetViewset(viewsets.ModelViewSet):
    queryset = Fleet.objects.all()
    serializer_class = FleetSerializer
	


	