from django_filters.rest_framework import DjangoFilterBackend		
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from api.models.siteroles import Siterole
from api.serializers.siteroles import SiteroleSerializer


class SiteroleViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = SiteroleSerializer
    queryset = Siterole.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('site','user')

