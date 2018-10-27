		
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from api.models.sitestatuses import Sitestatus
from api.serializers.sitestatuses import SitestatusSerializer


class SitestatusViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = SitestatusSerializer
    queryset = Sitestatus.objects.all()
