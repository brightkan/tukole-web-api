from rest_framework import serializers
from api.models.workspaces import Workspace 


class WorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace 
        fields = ('id','workspace_id','workspace_name','created_at','updated_at')	







		