from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel

from st_planets.constants import LONG_CHAR_FIELD_MAX_LENGTH


class Climate(TimeStampedModel):
    name = models.CharField(
        verbose_name=_("Name"), max_length=LONG_CHAR_FIELD_MAX_LENGTH, unique=True
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _("Planet")
        verbose_name_plural = _("Planets")


class Terrain(TimeStampedModel):
    name = models.CharField(
        verbose_name=_("Name"), max_length=LONG_CHAR_FIELD_MAX_LENGTH
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _("Terrain")
        verbose_name_plural = _("Terrains")


class Planet(TimeStampedModel):
    name = models.CharField(
        verbose_name=_("Name"), max_length=LONG_CHAR_FIELD_MAX_LENGTH
    )
    population = models.PositiveBigIntegerField(verbose_name=_("Population"))
    climates = models.ManyToManyField(
        to=Climate, related_name="planets", verbose_name=_("Climates")
    )
    terrains = models.ManyToManyField(
        to=Terrain, related_name="planets", verbose_name=_("Terrains")
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _("Planet")
        verbose_name_plural = _("Planets")
