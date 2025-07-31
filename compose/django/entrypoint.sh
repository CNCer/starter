#!/usr/bin/env bash

python manage.py collectstatic --noinput
#python manage.py migrate --noinput
# python manage.py triggers create
python -m gunicorn --bind 0.0.0.0:8000 --workers 3 config.wsgi:application
