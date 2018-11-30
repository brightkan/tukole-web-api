from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.models.reinstallation import ReInstallation
from api.serializers.reinstallation import ReInstallationSerializer


class ReInstallationViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = ReInstallation.objects.all()
    serializer_class = ReInstallationSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('site',)
