import csv

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
from datetime import date

from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND

from api.models import ManHole, User, ManHoleAssignment, ManHoleDuration, Site
from api.models.manholes import ManHoleInstallation, HandHoleInstallation, ODFInstallation
from api.serializers.manholes import ManHoleSerializer, ManHoleLoginSerializer, ManHoleAssignmentSerializer, \
    ManHoleCreateAssignmentSerializer, ManHoleUserFilterSerializer, ManHoleInstallationSerializer, \
    HandHoleInstallationSerializer, ManHoleUserImportSerializer, ManHoleImportSerializer, ODFInstallationSerializer


class ManHoleFilter(filters.FilterSet):
    user = filters.NumberFilter(method='filter_user_manhole')

    class Meta:
        model = ManHole
        fields = ['user', 'site', 'number']

    def filter_user_manhole(self, queryset, name, value):
        manhole_ids = ManHoleAssignment.objects.filter(user=value).values_list('manhole_id', flat=True)
        manholes = ManHole.objects.filter(id__in=manhole_ids)
        return manholes


class ManHoleViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = ManHole.objects.all()
    serializer_class = ManHoleSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = ManHoleFilter

    @action(methods=['post'], detail=True, url_path='login', url_name="login",
            serializer_class=ManHoleLoginSerializer)
    def manhole_login(self, request, pk):
        manhole_ = request.data['manhole']
        start_time = request.data['start_time']
        end_time = request.data['end_time']
        to_fibers = request.data['to_fibers']
        to_tube = request.data['to_tube']
        from_tube = request.data['from_tube']
        from_fibers = request.data['from_fibers']
        user_ = request.data['user']
        user = User.objects.filter(id=user_).first()
        manhole = ManHole.objects.filter(id=manhole_).first()

        if manhole and user:

            manhole_duraation = ManHoleDuration.objects.create(
                manhole=manhole,
                start_time=start_time,
                end_time=end_time,
                to_fibers=to_fibers,
                to_tube=to_tube,
                from_fibers=from_fibers,
                from_tube=from_tube,
                user=user)

            data = ManHoleLoginSerializer(manhole_duraation).data
        else:
            data = {"error": "Error logging into manhole", "status": False}
        return Response(data=data, status=HTTP_200_OK)

    @action(methods=['post'], detail=True, url_path='assign', url_name="assign",
            serializer_class=ManHoleCreateAssignmentSerializer)
    def manhole_assign(self, request, pk):
        user_ = request.data['user']
        manhole_ = request.data['manhole']
        manhole_assignment = ManHoleAssignment.objects.create(user_id=user_, manhole_id=manhole_)
        data = {
            "user": manhole_assignment.user.id,
            "manhole": manhole_assignment.manhole.id,

        }
        return Response(data=data, status=HTTP_200_OK)

    @action(methods=['post'], detail=False, url_path='assginimport', url_name="assginimport",
            serializer_class=ManHoleUserImportSerializer)
    def import_and_assign_manholes(self, request):
        csv_file_posted = request.data['file']
        user_id = request.data['user_assigned']
        site_id = request.data.get('site', None)
        user = User.objects.filter(id=user_id).first()
        site = Site.objects.filter(id=site_id).first()
        if user:
            csv_file = StringIO(csv_file_posted.read().decode())
            csv_reader = csv.reader(csv_file, delimiter=',')
            title = next(csv_reader)
            man_holes = next(csv_reader)
            count = 0
            for row in man_holes:
                if row.startswith('G:'):
                    manhole_ = row
                    manhole_ = manhole_.split(':')[1]
                    manhole_ = manhole_.split('_')[0]
                    manhole, manhole_created = ManHole.objects.get_or_create(number=manhole_, site=site)
                    manhole_assignment, assignment_created = ManHoleAssignment.objects.get_or_create(user=user,
                                                                                                     manhole=manhole)
                    if manhole_created and assignment_created:
                        count = count + 1
            data = {'number_of_manholes_assgined': count, 'user_id': user.id}
            return Response(data=data, status=HTTP_200_OK)
        else:
            data = {'status': False, 'error': 'No user with that id found'}
            return Response(data=data, status=HTTP_404_NOT_FOUND)

    @action(methods=['post'], detail=False, url_path='import', url_name="import",
            serializer_class=ManHoleImportSerializer)
    def import_manholes(self, request):
        csv_file_posted = request.data['file']
        site_id = request.data.get('site', None)
        site = Site.objects.filter(id=site_id).first()
        csv_file = StringIO(csv_file_posted.read().decode())
        csv_reader = csv.reader(csv_file, delimiter=',')
        title = next(csv_reader)
        man_holes = next(csv_reader)
        count = 0
        for row in man_holes:
            if row.startswith('G:'):
                manhole_ = row
                manhole_ = manhole_.split(':')[1]
                manhole_ = manhole_.split('_')[0]
                manhole, manhole_created = ManHole.objects.get_or_create(number=manhole_, defaults={'site': site})
                if manhole_created:
                    count = count + 1
        data = {'number_of_manholes': count, }
        return Response(data=data, status=HTTP_200_OK)


class ManHoleAssignmentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = ManHoleAssignment.objects.all()
    serializer_class = ManHoleAssignmentSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('user', 'manhole')

    def get_queryset(self):
        today = date.today()
        manhole_today = ManHoleAssignment.objects.filter(created__year=today.year, created__month=today.month,
                                                         created__day=today.day)
        return manhole_today

    @action(methods=['get'], detail=False, url_path='all', url_name="all",
            serializer_class=ManHoleUserFilterSerializer)
    def all_manhole_assignments(self, request):
        manholes_today = ManHoleAssignment.objects.all()
        filtered_manhole = self.filter_queryset(manholes_today)
        data = ManHoleAssignmentSerializer(filtered_manhole, many=True).data
        return Response(data=data, status=HTTP_200_OK)


class ManHoleDurationViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = ManHoleDuration.objects.all()
    serializer_class = ManHoleLoginSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('user', 'manhole')


class ManHoleInstallationViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = ManHoleInstallation.objects.all()
    serializer_class = ManHoleInstallationSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('user', 'site')


class HandHoleInstallationViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = HandHoleInstallation.objects.all()
    serializer_class = HandHoleInstallationSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('user', 'site')


class ODFInstallationViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = ODFInstallation.objects.all()
    serializer_class = ODFInstallationSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('user', 'site')
