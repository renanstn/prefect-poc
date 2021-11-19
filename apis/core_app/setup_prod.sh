#!/bin/sh

python manage.py collectstatic --noinput;
python manage.py makemigrations;
python manage.py migrate --noinput --check;

uvicorn core_app.asgi:application --host 0.0.0.0 --port 80
