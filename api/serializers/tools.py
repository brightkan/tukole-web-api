from rest_framework import serializers

from api.models.tools import Tool


class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = ('id', 'name', 'type', 'uuid', 'humanUuid','status','workspace', 'created', 'modified')
