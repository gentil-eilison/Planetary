from django_filters import rest_framework as filters

from ..models import Climate


class ClimateFilterSet(filters.FilterSet):
    name = filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Climate
        fields = ("name",)
