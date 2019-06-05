from rest_framework import serializers

from api.models.activities import Activity


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('id', 'title', 'description', 'created', 'site', 'user', 'start_time',
                  'end_time', 'duration', 'image')
