# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.models.notifications import Notification
from api.serializers.notifications import NotificationSerializer


# Create your views here.
# from your_app_name.models import Dodavatel
# p = Dodavatel(nazov='Petr', dostupnost=1)
# p.save()


class NotificationViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('user',)
