# Create your views here.

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.models.machinery import Machinery
from api.serializers.machinery import MachinerySerializer


# Create your views here.

class MachineryViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Machinery.objects.all()
    serializer_class = MachinerySerializer
