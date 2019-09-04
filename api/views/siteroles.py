import csv

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import ModelViewSet

from api.models import Site, User

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from api.models.siteroles import Siterole
from api.serializers.siteroles import SiteroleSerializer, SiteRoleImportSerializer


class SiteroleViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = SiteroleSerializer
    queryset = Siterole.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('site', 'user')

    @action(
        methods=['post'],
        detail=False,
        url_path='import',
        url_name="import",
        serializer_class=SiteRoleImportSerializer,
    )
    def import_site_roles(self, request):
        csv_file_posted = request.data['file']
        csv_file = StringIO(csv_file_posted.read().decode())
        csv_reader = csv.reader(csv_file, delimiter=',')
        count = 0
        for row in csv_reader:
            site_name_ = row[0]
            isp = row[1]
            osp = row[2]
            surveyor = row[3]
            site = Site.objects.filter(site_name__icontains=site_name_).first()
            if site_name_ and site:
                isp_user = User.objects.filter(email=isp).first()
                osp_user = User.objects.filter(email=osp).first()
                surveyor_user = User.objects.filter(email=surveyor).first()
                if isp and isp_user:
                    site_role_, created = Siterole.objects.get_or_create(
                        site=site, user=isp_user, role='ISP'
                    )
                    if created:
                        count = count + 1
                elif osp and osp_user:
                    site_role_, created = Siterole.objects.get_or_create(
                        site=site, user=osp_user, role='OSP'
                    )
                    if created:
                        count = count + 1
                elif surveyor and surveyor_user:
                    site_role_, created = Siterole.objects.get_or_create(
                        site=site, user=surveyor_user, role='Surveyor'
                    )
                    if created:
                        count = count + 1
        data = {'status': True, 'count_of_site_roles': count}
        return Response(data=data, status=HTTP_200_OK)
