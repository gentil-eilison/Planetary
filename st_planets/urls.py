from django.contrib import admin
from django.urls import URLPattern, URLResolver, include, path
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView,
                                   SpectacularSwaggerView)

from st_planets.api_router import get_api_urls

urlpatterns: list[URLResolver | URLPattern] = [
    path("admin/", admin.site.urls),
    path("api/", include(get_api_urls())),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
