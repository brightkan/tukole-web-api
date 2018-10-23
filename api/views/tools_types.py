# Create your views here.

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.models.tools_types import ToolType
from api.serializers.tools_types import ToolTypesSerializer


# Create your views here.
class Tools_typesViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = ToolType.objects.all()
    serializer_class = ToolTypesSerializer
