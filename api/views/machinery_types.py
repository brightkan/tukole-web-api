	
# Create your views here.

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.models.machinery_types import MachineryType
from api.serializers.machinery_types import MachineryTypeSerializer


# Create your views here.

class MachineryTypeViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = MachineryType.objects.all()
    serializer_class = MachineryTypeSerializer
  

