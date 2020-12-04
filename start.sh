#!/bin/bash

source ~/.bashrc
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser --noinput --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL
service apache2 restart
gunicorn servicioplanificacion.wsgi
