#!/bin/sh

black .
python manage.py collectstatic --noinput;
python manage.py makemigrations;
python manage.py migrate;
python manage.py createadmin;

uvicorn core_app.asgi:application --host 0.0.0.0 --port 80 --reload
