from rest_framework import serializers

from api.models.comments import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'title', 'description', 'created', 'affected_teams', 'site', 'priority',
                  'user', 'status', 'fixed_at', 'appraisal')
