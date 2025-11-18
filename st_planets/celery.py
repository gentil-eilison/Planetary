import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "st_planets.settings")

app = Celery("st_planets")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
