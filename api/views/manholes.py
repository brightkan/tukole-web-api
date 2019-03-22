from datetime import date

from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from api.models import ManHole, User, ManHoleAssignment, ManHoleDuration
from api.models.manholes import ManHoleInstallation, HandHoleInstallation
from api.serializers.manholes import ManHoleSerializer, ManHoleLoginSerializer, ManHoleAssignmentSerializer, \
    ManHoleCreateAssignmentSerializer, ManHoleUserFilterSerializer, ManHoleInstallationSerializer, \
    HandHoleInstallationSerializer


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
        user_ = request.data['user']
        user = User.objects.filter(id=user_).first()
        manhole = ManHole.objects.filter(id=manhole_).first()

        if manhole and user:
            manhole_duraation = ManHoleDuration.objects.create(
                manhole=manhole,
                start_time=start_time,
                end_time=end_time,
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
