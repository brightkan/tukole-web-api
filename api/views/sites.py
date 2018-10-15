	
from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from api.models.sites import Sites
from api.serializers.sites import SitesSerializer

# Create your views here.

class SitesViewset(viewsets.ModelViewSet):
    queryset = Sites.objects.all()
    serializer_class = SitesSerializer
