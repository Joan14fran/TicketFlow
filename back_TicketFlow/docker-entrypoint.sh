#!/bin/sh

echo "--> Iniciando Entrypoint..."

# Aplicar migraciones
echo "--> Aplicando migraciones de Django..."
python manage.py makemigrations
python manage.py migrate --noinput

echo "--> Iniciando Servidor..."
exec "$@"