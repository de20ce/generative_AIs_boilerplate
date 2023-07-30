#!/bin/sh
# fails if any command in your code fails
set -o errexit
# exit if any of pipe command fails
set -o pipefail
# exit if any variable is not set
set -o nounset

# postgres database setup
postgres_ready() {
# python code that connects to postgres container over psycopg2  
python << END
import sys
import psycopg2
try:
    psycopg2.connect(
    dbname="${SQL_DATABASE}",
    user="${SQL_USER}",
    password="${SQL_PASSWORD}",
    host="${SQL_HOST}",
    port="${SQL_PORT}",
    )
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}
until postgres_ready; do
    >&2 echo 'Waiting for postgreSQL...'
    sleep 10
done

>&2 echo 'PostgreSQL starts!'

python manage.py makemigrations
python manage.py migrate
daphne -b 0.0.0.0 -p 8000 core.asgi:application