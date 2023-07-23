#!/bin/sh
# make sure you start postgres instance somewhere with the good parameters
# you should set your env files correctly as well!
echo 'waiting for postgres...'

while ! nc -z $SQL_HOST $SQL_PORT; do
    sleep 0.2
done

echo 'PostgreSQL started!'

echo 'Running migrations...'
python manage.py migrate

echo 'Migration done!'

echo 'Collecting static files...'
python manage.py collectstatic --no-input

echo 'Static files Collected!'

echo 'starting the server...'
daphne -b 0.0.0.0 -p 8000 core.asgi:application

echo 'Server starts!'