# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.models import Comment, User
# Create your views here.
from api.models.notifications import Notification
from api.models.siteroles import Siterole
from api.serializers.comment import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('site', 'user', 'status', 'appraisal')

    def perform_create(self, serializer):
        super().perform_create(serializer)
        affected_teams = serializer['affected_teams']
        site = serializer['site']
        description = serializer['description']
        affected_teams = str(affected_teams)
        affected_teams = affected_teams.split(',')
        for team in affected_teams:
            user_ids = Siterole.objects.filter(site_id=site, role=team).values_list('user_id', flat=True)
            users = User.objects.filter(id__in=user_ids)
            for user in users:
                Notification.objects.create(description=description, user=user)
