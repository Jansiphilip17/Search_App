#!/usr/bin/env bash
set -e

python manage.py migrate --noinput
python manage.py load_website_data
gunicorn techpanda_project.wsgi:application --bind 0.0.0.0:"$PORT"
