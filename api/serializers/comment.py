from rest_framework import serializers

from api.models.challenges import Challenge
from api.models.comments import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'title', 'description', 'created', 'affected_teams', 'site', 'priority', 'user')
