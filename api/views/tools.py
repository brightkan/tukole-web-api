# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.models.tools import Tool
from api.serializers.tools import ToolSerializer


# Create your views here.

class ToolsViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('workspace','type')
