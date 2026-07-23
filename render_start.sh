#!/usr/bin/env bash

python manage.py migrate
python manage.py collectstatic --noinput
exec gunicorn techpanda_project.wsgi:application