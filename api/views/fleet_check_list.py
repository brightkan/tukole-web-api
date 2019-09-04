from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from api.models import FleetCheckListItem, FleetCheckList, FleetCheckListItemResult
from api.serializers.fleet_check_list import (
    FleetCheckListItemSerializer,
    FleetCheckListSerializer,
    FleetCheckListItemResultSerializer,
    FleetCheckResultCreateSerializer,
)


class FleetCheckListItemViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = FleetCheckListItem.objects.all()
    serializer_class = FleetCheckListItemSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('workspace',)


class FleetCheckListViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = FleetCheckList.objects.all()
    serializer_class = FleetCheckListSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('fleet', 'workspace')


class FleetCheckListItemResultViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = FleetCheckListItemResult.objects.all()
    serializer_class = FleetCheckListItemResultSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id',)

    @action(
        methods=['post'],
        detail=False,
        url_path='results',
        url_name="results",
        serializer_class=FleetCheckResultCreateSerializer,
    )
    def create_checklist_results(self, request):
        status = request.data['status']
        request_object_id = request.data['request_object_id']
        check_list_items = request.data['check_list_items']

        ids = check_list_items.split(',')
        count = 0
        for id in ids:
            fl, created = FleetCheckListItemResult.objects.get_or_create(
                status=status, request_object_id_id=request_object_id, fleet_check_list_item_id=id
            )
            if created:
                count = count + 1
        data = {'status': True, 'check_list_items_saved': count}
        return Response(data=data, status=HTTP_200_OK)
