#!/bin/sh

exec celery -A st_planets.celery worker --loglevel=INFO
