# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.models import Trip
# Create your views here.
from api.serializers.trips import TripSerializer


class TripViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('site_fleet',)
