from rest_framework import serializers
from api.models.tools_types import Tools_types
		
##//////////////////
class Tools_typesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tools_types
        fields = ('id', 'type', 'description')

