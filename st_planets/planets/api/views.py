from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.request import HttpRequest
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from st_planets.core.mixins import CreateReadSerializerMixin
from st_planets.planets.api import filters, serializers

from ..models import Climate, Planet, Terrain
from ..tasks import collect_planets_data


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


class RefreshPlanetsDataView(APIView):
    http_method_names = ["post"]

    def post(self, request: HttpRequest, format=None) -> Response:
        collect_planets_data.delay()
        return Response(
            data={"message": "Data collection started!"},
            status=status.HTTP_202_ACCEPTED,
        )
