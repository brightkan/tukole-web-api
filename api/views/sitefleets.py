from django_filters.rest_framework import DjangoFilterBackend		
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from api.models.sitefleets import Sitefleet
from api.serializers.sitefleets import SitefleetSerializer


class SitefleetViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = SitefleetSerializer
    queryset = Sitefleet.objects.all()

