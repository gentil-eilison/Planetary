from django.db import models, transaction
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel

from st_planets.constants import LONG_CHAR_FIELD_MAX_LENGTH

from .typing import PlanetResponse


class Climate(TimeStampedModel):
    name = models.CharField(
        verbose_name=_("Name"), max_length=LONG_CHAR_FIELD_MAX_LENGTH, unique=True
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _("Climate")
        verbose_name_plural = _("Climates")


class Terrain(TimeStampedModel):
    name = models.CharField(
        verbose_name=_("Name"), max_length=LONG_CHAR_FIELD_MAX_LENGTH, unique=True
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _("Terrain")
        verbose_name_plural = _("Terrains")


class Planet(TimeStampedModel):
    name = models.CharField(
        verbose_name=_("Name"), max_length=LONG_CHAR_FIELD_MAX_LENGTH, unique=True
    )
    population = models.PositiveBigIntegerField(verbose_name=_("Population"), null=True)
    climates = models.ManyToManyField(
        to=Climate, related_name="planets", verbose_name=_("Climates")
    )
    terrains = models.ManyToManyField(
        to=Terrain, related_name="planets", verbose_name=_("Terrains")
    )

    @staticmethod
    @transaction.atomic
    def create_from_planet_list(planets: list[PlanetResponse]) -> None:
        planets_objs: list[Planet] = []
        planets_climates: dict[str, models.QuerySet[Climate]] = {}
        planets_terrains: dict[str, models.QuerySet[Terrain]] = {}
        planets_names: list[str] = []
        for planet in planets:
            name, population = planet.get("name"), planet.get("population")
            planets_objs.append(
                Planet(
                    name=name,
                    population=population,
                )
            )
            planets_names.append(name)
            climates: list[str] | None = planet.get("climates")
            if climates:
                planets_climates.update(
                    {name: Climate.objects.filter(name__in=climates)}
                )
            terrains: list[str] | None = planet.get("terrains")
            if terrains:
                planets_terrains.update(
                    {name: Terrain.objects.filter(name__in=terrains)}
                )

        Planet.objects.bulk_create(planets_objs, ignore_conflicts=False)

        db_planets = Planet.objects.filter(name__in=list(planets_names))
        for planet in db_planets:
            planet.climates.set(planets_climates.get(planet.name) or [])
            planet.terrains.set(planets_terrains.get(planet.name) or [])
            planet.save()

    def get_climates_names(self) -> list[str]:
        return list(self.climates.values_list("name", flat=True))

    def get_terrains_names(self) -> list[str]:
        return list(self.terrains.values_list("name", flat=True))

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _("Planet")
        verbose_name_plural = _("Planets")
