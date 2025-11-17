from django.urls import URLResolver
from rest_framework import routers

from st_planets.planets.api import views

app_name: str = "planets"
router: routers.SimpleRouter = routers.SimpleRouter()
router.register(r"climates", views.ClimateViewSet)

urlpatterns: list[URLResolver] = router.urls
