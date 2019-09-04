from rest_framework import serializers

from api.models.tools_types import ToolType


class ToolTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToolType
        fields = ('id', 'type', 'description', 'workspace')
