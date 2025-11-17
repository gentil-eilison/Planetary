from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from st_planets.core.mixins import CreateReadSerializerMixin
from st_planets.planets.api import filters, serializers

from ..models import Climate, Planet, Terrain


class ClimateViewSet(ModelViewSet):
    serializer_class = serializers.ClimateSerializer
    queryset = Climate.objects.all()
    filterset_class = filters.ClimateFilterSet
    permission_classes = (AllowAny,)


class TerrainViewSet(ModelViewSet):
    serializer_class = serializers.TerrainSerializer
    queryset = Terrain.objects.all()
    filterset_class = filters.TerrainFilterSet
    permission_classes = (AllowAny,)


class PlanetViewSet(CreateReadSerializerMixin, ModelViewSet):
    queryset = Planet.objects.all().prefetch_related("climates", "terrains")
    permission_classes = (AllowAny,)
    filterset_class = filters.PlanetFilterSet
    read_serializer_class = serializers.PlanetReadSerializer
    create_serializer_class = serializers.PlanetCreateSerializer
