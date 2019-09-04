# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.models import Incident

# Create your views here.
from api.serializers.incidents import IncidentSerializer


class IncidentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('site', 'user')
