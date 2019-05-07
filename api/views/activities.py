# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.models.activities import Activity
from api.serializers.activities import ActivitySerializer


class ActivityViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('site', 'user')
