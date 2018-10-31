from django_filters.rest_framework import DjangoFilterBackend				
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from api.models.siteboqs import Siteboq
from api.serializers.siteboqs import SiteboqSerializer


class SiteboqViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = SiteboqSerializer
    queryset = Siteboq.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('site','material','user')


    
	
