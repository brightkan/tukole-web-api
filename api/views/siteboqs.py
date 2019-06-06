from django.db.models import Sum
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import ModelViewSet

from api.models import Site, Material
from api.models.siteboqs import Siteboq
from api.serializers.siteboqs import SiteboqSerializer


class DistinctSum(Sum):
    function = "SUM"
    template = "%(function)s(DISTINCT %(expressions)s)"


class SiteboqViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = SiteboqSerializer
    queryset = Siteboq.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('site', 'material', 'user')

    @action(methods=['get'], detail=True, url_path='summary', url_name="summary", )
    def get_siteboq_summary(self, request, pk):
        # improve this
        site = Site.objects.filter(id=pk).first()
        data = []
        if site:
            boqs = Siteboq.objects.filter(site_id=site.id).values_list('material__id', flat=True).distinct()
            for boq in boqs:
                material = Material.objects.get(id=boq)
                bq = Siteboq.objects.filter(material__name=material.name, site_id=site.id).aggregate(
                    total_actual_quantity=Sum('actual_quantity'),
                    total_estimate_quantity=Sum(
                        'estimate_quantity'),
                )
                siteboq = Siteboq.objects.filter(material__name=material.name).last()
                boq_type = siteboq.boq_type
                description = siteboq.description
                site = siteboq.site

                siteboq_data = {
                    'site': site.id,
                    'description': description,
                    'material': material.name,
                    'boq_type': boq_type,
                    'total_actual_quantity': bq['total_actual_quantity'],
                    'total_estimate_quantity': bq['total_estimate_quantity'],
                    'measurement_unit': material.measurement,
                    'unit_cost': material.measurement,

                }
                data.append(siteboq_data)
            return Response(data=data, status=HTTP_200_OK)
        else:
            return Response(data=data, status=HTTP_200_OK)
