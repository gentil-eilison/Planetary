from rest_framework import serializers

from ..models import Climate, Terrain


class ClimateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Climate
        fields = ("id", "name")
        extra_kwargs = {"id": {"read_only": True}}


class TerrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terrain
        fields = ("id", "name")
        extra_kwargs = {"id": {"read_only": True}}
