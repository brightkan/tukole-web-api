from rest_framework import serializers

from api.models.tools import Tools


class ToolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tools
        fields = ('id', 'name', 'type', 'uuid', 'humanUuid', 'workspace_id', 'created_at', 'updated_at')
