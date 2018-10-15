from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from api.models.tools_types import Tools_types
from api.serializers.tools_types import Tools_typesSerializer
	
# Create your views here.
class Tools_typesViewset(viewsets.ModelViewSet):
    queryset = Tools_types.objects.all()
    serializer_class = Tools_typesSerializer
	
