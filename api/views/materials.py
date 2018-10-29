from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from api.models.materials import Material
from api.serializers.materials import MaterialSerializer


class MaterialViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('workspace',)

