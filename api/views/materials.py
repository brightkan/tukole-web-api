import csv

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import ModelViewSet

from api.models import Workspace
from api.models.materials import Material
from api.serializers.materials import MaterialSerializer
from api.serializers.warehousematerials import MaterialImportSerializer


class MaterialViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('workspace', 'running_out')

    @action(methods=['post'], detail=False, url_path='import', url_name="import",
            serializer_class=MaterialImportSerializer)
    def import_manholes(self, request):
        csv_file_posted = request.data['file']
        workspace_id = request.data.get('workspace', None)
        workspace = Workspace.objects.filter(id=workspace_id).first()
        csv_file = StringIO(csv_file_posted.read().decode())
        csv_reader = csv.reader(csv_file, delimiter=',')
        title = next(csv_reader)
        count = 0
        for row in csv_reader:
            measure = row[4]
            if float(row[3]) < 10.0000:
                Material.objects.get_or_create(name=row[2], defaults={"measurement": row[4], "quantity": row[3],
                                                                      'running_out': True, 'workspace': workspace})
            else:
                Material.objects.get_or_create(name=row[2],
                                               defaults={"measurement": row[4], "quantity": row[3],
                                                         'workspace': workspace})
            count = count + 1
        data = {'number_of_materials': count, }
        return Response(data=data, status=HTTP_200_OK)
