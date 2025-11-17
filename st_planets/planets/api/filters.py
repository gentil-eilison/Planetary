from django_filters import rest_framework as filters

from st_planets.core.filter_fields import StringInFilter

from ..models import Climate, Planet, Terrain


class ClimateFilterSet(filters.FilterSet):
    name = filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Climate
        fields = ("name",)


class TerrainFilterSet(filters.FilterSet):
    name = filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Terrain
        fields = ("name",)


class PlanetFilterSet(filters.FilterSet):
    name = filters.CharFilter(lookup_expr="icontains")
    population_gt = filters.NumberFilter(field_name="population", lookup_expr="gt")
    population_lt = filters.NumberFilter(field_name="population", lookup_expr="lt")
    climates = StringInFilter(field_name="climates__name")
    terrains = StringInFilter(field_name="terrains__name")

    class Meta:
        model = Planet
        fields = ("name",)
