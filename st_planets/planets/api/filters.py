from django_filters import rest_framework as filters

from ..models import Climate, Terrain


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
