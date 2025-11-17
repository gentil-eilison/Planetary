from rest_framework import serializers

from ..models import Climate


class ClimateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Climate
        fields = ("id", "name")
        extra_kwargs = {"id": {"read_only": True}}
