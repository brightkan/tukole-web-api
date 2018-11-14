from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from api.models.sitemachines import SiteMachines
from api.serializers.sitemachines import SiteMachinesSerializer


class SiteMachinesViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = SiteMachinesSerializer
    queryset = SiteMachines.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('site', 'machine')
