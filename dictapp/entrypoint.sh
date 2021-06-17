#!/bin/sh

python manage.py migrate

gunicorn dictapp.wsgi:application --bind 0.0.0.0:$PORT