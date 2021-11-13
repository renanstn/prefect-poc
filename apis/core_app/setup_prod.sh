#!/bin/sh

python manage.py makemigrations;
python manage.py migrate;

uvicorn core_app.asgi:application --host 0.0.0.0 --port 80
