# Movie App

## Installation

### Backend

    docker-compose up -d --build
    docker-compose exec backend python api/manage.py createsuperuser

### Postgres

    docker-compose exec db psql -d api -U backend -f /var/lib/postgresql/script/init.sql

## Test

### Backend

    docker-compose exec backend python api/manage.py test movies
