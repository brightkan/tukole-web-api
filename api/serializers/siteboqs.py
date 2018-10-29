	
from rest_framework import serializers

from api.models.siteboqs import Siteboq


class SiteboqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Siteboq
        fields = ('id', 'site', 'material', 'quantity', 'boq_type', 'user')

    
	
