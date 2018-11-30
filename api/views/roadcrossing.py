from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.models.roadcrossing import RoadCrossing
from api.serializers.roadcrossing import RoadCrossingSerializer


class RoadCrossingViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = RoadCrossing.objects.all()
    serializer_class = RoadCrossingSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('site',)
