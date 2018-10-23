# Create your views here.

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.models.sites import Site
from api.serializers.sites import SiteSerializer


# Create your views here.

class SitesViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
