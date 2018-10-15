		
from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from api.models.machinerys import Machinery
from api.serializers.machinerys import MachinerySerializer
	
# Create your views here.

class MachineryViewset(viewsets.ModelViewSet):
    queryset = Machinery.objects.all()
    serializer_class = MachinerySerializer
	
		






		