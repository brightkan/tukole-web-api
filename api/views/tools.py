# Create your views here.

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.models.tools import Tools
from api.serializers.tools import ToolsSerializer


# Create your views here.

class ToolsViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Tools.objects.all()
    serializer_class = ToolsSerializer
