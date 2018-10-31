from rest_framework import serializers

from api.models.workspaces import Workspace


class WorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = ('id', 'name', 'created', 'modified', 'created')
