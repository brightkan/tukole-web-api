# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.models.machinery import Machinery
from api.serializers.machinery import MachinerySerializer


# Create your views here.


class MachineryViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Machinery.objects.all()
    serializer_class = MachinerySerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('workspace', 'type')
