		
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from api.models.sitereports import Sitereport
from api.serializers.sitereports import SitereportSerializer


class SitereportViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = SitereportSerializer
    queryset = Sitereport.objects.all()

