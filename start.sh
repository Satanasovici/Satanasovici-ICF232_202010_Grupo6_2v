#!/bin/bash

source ~/.bashrc
python manage.py makemigrations
python manage.py migrate


