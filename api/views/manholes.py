from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from api.models import ManHole, User, ManHoleAssignment
from api.serializers.manholes import ManHoleSerializer, ManHoleLoginSerializer, ManHoleAssignmentSerializer


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
        duration = request.data['duration']
        user_ = request.data['user']
        user = User.objects.filter(id=user_).first()
        manhole = ManHole.objects.filter(id=manhole_).first()

        if manhole and user:
            user = ManHole.objects.create(
                manhole=manhole,
                duration=duration,
                user=user)
            data = ManHoleLoginSerializer(manhole=manhole_, duration=duration, user_=user).data
        else:
            data = {"error": "Error logging into manhole", "status": False}
        return Response(data=data, status=HTTP_200_OK)

    @action(methods=['post'], detail=True, url_path='assign', url_name="assign",
            serializer_class=ManHoleAssignmentSerializer)
    def manhole_assign(self, request, pk):
        user_ = request.data['user']
        manhole_ = request.data['manhole']
        manhole_assignment = ManHoleAssignment.objects.create(user_id=user_, manhole_id=manhole_)
        data = {
            "user": manhole_assignment.user.id,
            "manhole": manhole_assignment.manhole.id,

        }
        return Response(data=data, status=HTTP_200_OK)
