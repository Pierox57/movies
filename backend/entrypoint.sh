#!/bin/sh
python /app/api/manage.py migrate
python /app/api/manage.py collectstatic --no-input
python /app/api/manage.py loaddata movies.json

gunicorn --chdir /app/api api.wsgi:application -b 0.0.0.0:8000