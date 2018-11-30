from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.models import ManHole
from api.serializers.manholes import ManHoleSerializer


class ManHoleViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = ManHole.objects.all()
    serializer_class = ManHoleSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('site',)
