import json
import logging
from typing import Any, Final, cast

import requests
from celery import shared_task

from .models import Planet
from .typing import PlanetResponse

logger = logging.getLogger(__name__)


@shared_task
def collect_planets_data():
    URL: Final[str] = (
        "https://swapi-graphql.netlify.app/.netlify/functions/index?query=query%20Query%20{allPlanets{planets{name%20population%20terrains%20climates}}}"
    )
    try:
        response = requests.get(URL)
        body: dict[str, Any] = response.json()

        if body:
            data = body.get("data")
            if data:
                allPlanets = cast(dict[str, dict[str, Any]], data).get("allPlanets")
                if allPlanets:
                    planets: list[PlanetResponse] = cast(
                        list[PlanetResponse], allPlanets.get("planets")
                    )
                    Planet.create_from_planet_list(planets)

    except json.JSONDecodeError as e:
        logging.error(f"Body is not json: {e}")
    except Exception as e:
        logging.error(f"Couldn't complete request: {e}")
