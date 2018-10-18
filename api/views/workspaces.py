from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from api.models.workspaces import Workspace
from api.serializers.workspaces import WorkspaceSerializer
	
# Create your views here.

class WorkspaceViewset(viewsets.ModelViewSet):
    queryset = Workspace.objects.all()
    serializer_class = WorkspaceSerializer
	


	