from rest_framework.serializers import ModelSerializer

from api.models.materials import Material


class MaterialSerializer(ModelSerializer):
    class Meta:
        model = Material
        fields = ('id', 'name', 'workspace')
