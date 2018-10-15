# Create your views here.

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.models.tools_types import Tools_types
from api.serializers.tools_types import Tools_typesSerializer


# Create your views here.
class Tools_typesViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Tools_types.objects.all()
    serializer_class = Tools_typesSerializer
