from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from api.models.sitetools import Sitetool
from api.serializers.sitetools import SitetoolSerializer


class SitetoolViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = SitetoolSerializer
    queryset = Sitetool.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('tool','site','user')

		