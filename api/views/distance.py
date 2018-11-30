from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.models.distance import TrenchedDistance
from api.serializers.distance import TrenchedDistanceSerializer


class TrenchedDistanceViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = TrenchedDistance.objects.all()
    serializer_class = TrenchedDistanceSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('site',)
