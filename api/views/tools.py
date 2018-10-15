# Create your views here.

from rest_framework import viewsets

from api.models.tools import Tools
from api.serializers.tools import ToolsSerializer


# Create your views here.

class ToolsViewset(viewsets.ModelViewSet):
    queryset = Tools.objects.all()
    serializer_class = ToolsSerializer
