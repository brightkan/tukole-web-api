# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.models.notifications import Notification
from api.models.sites import Site, SiteImage
from api.serializers.sites import SiteSerializer, SiteImageSerializer


# Create your views here. user=Site.clientId,

class SitesViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('workspace', 'clientId')

    def get_context_data(self, **kwargs):
        user = Site.objects.get(id=kwargs['user_id'])
        p = Notification(notification=user)
        p.save()


class SiteImageViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = SiteImage.objects.all()
    serializer_class = SiteImageSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('site','status')
