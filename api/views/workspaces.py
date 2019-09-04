# Create your views here.

from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from api.models.workspaces import Workspace
from api.serializers.workspaces import WorkspaceSerializer


# Create your views here.


class WorkspaceViewset(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Workspace.objects.all()
    serializer_class = WorkspaceSerializer
