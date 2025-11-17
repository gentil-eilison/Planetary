from importlib import import_module

from django.apps import apps
from django.urls import URLResolver


def get_api_urls() -> list[URLResolver]:
    all_patterns: list[URLResolver] = []
    for app_config in apps.get_app_configs():
        try:
            if app_config.module:
                qualified_name: str = app_config.module.__name__ + ".api.urls"
                urls_module = import_module(qualified_name)
                all_patterns += urls_module.urlpatterns
        except ImportError:
            pass

    return all_patterns
