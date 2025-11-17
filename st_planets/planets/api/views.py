from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from st_planets.planets.api import filters, serializers

from ..models import Climate, Terrain


class ClimateViewSet(ModelViewSet):
    serializer_class = serializers.ClimateSerializer
    queryset = Climate.objects.all().prefetch_related("planets")
    filterset_class = filters.ClimateFilterSet
    permission_classes = (AllowAny,)


class TerrainViewSet(ModelViewSet):
    serializer_class = serializers.TerrainSerializer
    queryset = Terrain.objects.all().prefetch_related("planets")
    filterset_class = filters.TerrainFilterSet
    permission_classes = (AllowAny,)
