from rest_framework import serializers

from ..models import Climate, Planet, Terrain


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


class PlanetCreateSerializer(serializers.ModelSerializer):
    climates = serializers.PrimaryKeyRelatedField(
        queryset=Climate.objects.all(),
        many=True,
        allow_empty=True,
        required=False,
    )
    terrains = serializers.PrimaryKeyRelatedField(
        queryset=Terrain.objects.all(),
        many=True,
        allow_empty=True,
        required=False,
    )

    class Meta:
        model = Planet
        fields = ("name", "population", "climates", "terrains")


class PlanetReadSerializer(serializers.ModelSerializer):
    climates = ClimateSerializer(many=True)
    terrains = TerrainSerializer(many=True)

    class Meta:
        model = Planet
        fields = ("id", "name", "population", "climates", "terrains")
