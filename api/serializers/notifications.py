	
from rest_framework import serializers

from api.models.notifications import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('id', 'user', 'notification','read', 'created')
