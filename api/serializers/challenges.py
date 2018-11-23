from rest_framework import serializers

from api.models.challenges import Challenge


class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = ('id', 'title', 'description', 'created', 'type', 'site', 'user')
