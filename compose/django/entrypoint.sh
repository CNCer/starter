#!/usr/bin/env bash

python manage.py collectstatic --noinput
#python manage.py migrate --noinput
#python -m gunicorn --bind 0.0.0.0:8000 --workers 3 config.wsgi:application
#python -m gunicorn --bind 0.0.0.0:8000 --workers $WEB_CONCURRENCY config.wsgi:application

python -m gunicorn --bind 0.0.0.0:8000 --workers $GUNICOEN_WORKERS --threads $GUNICOEN_THREAD config.wsgi:application

