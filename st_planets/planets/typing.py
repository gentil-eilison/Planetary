from typing import TypedDict


class PlanetResponse(TypedDict):
    name: str
    population: str | None
    terrains: list[str] | None
    climates: list[str] | None
