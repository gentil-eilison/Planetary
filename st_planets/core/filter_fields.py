from django_filters import rest_framework as filters


class StringInFilter(filters.BaseInFilter, filters.CharFilter):
    pass
