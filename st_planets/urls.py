from django.contrib import admin
from django.urls import URLResolver, include, path

from st_planets.api_router import get_api_urls

urlpatterns: list[URLResolver] = [
    path("admin/", admin.site.urls),
    path("api/", include(get_api_urls())),
]
