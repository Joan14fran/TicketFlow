#!/bin/bash
set -e

echo "migraciones..."
python manage.py migrate --noinput

echo "servidor Django..."
exec python manage.py runserver 0.0.0.0:8000