from rest_framework import serializers

from api.models.tools import Tool, ToolAssignment


class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = (
            'id',
            'name',
            'type',
            'uuid',
            'humanUuid',
            'status',
            'workspace',
            'created',
            'modified',
            'assigned_to',
        )


class ToolAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToolAssignment
        fields = ('id', 'user', 'tool', 'created')
