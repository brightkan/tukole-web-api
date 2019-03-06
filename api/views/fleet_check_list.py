from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.models import FleetCheckListItem, FleetCheckList
from api.serializers.fleet_check_list import FleetCheckListItemSerializer, FleetCheckListSerializer


class FleetCheckListItemViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = FleetCheckListItem.objects.all()
    serializer_class = FleetCheckListItemSerializer


class FleetCheckListViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = FleetCheckList.objects.all()
    serializer_class = FleetCheckListSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('fleet','workspace')
