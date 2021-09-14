# Movie App

## Installation

Create a **.env** file in **backend/** and write bellow text :
    
    SECRET_KEY=<secret_key>
    DEBUG=<boolean>
    POSTGRES_DB=<db_name>
    POSTGRES_USER=<username>
    POSTGRES_PASSWORD=<password>
    CELERY_BROKER=redis://redis:6379/0
    CELERY_BACKEND=redis://redis:6379/0

Create an other **.env** file un **postgres/** and write bellow text :
    
    POSTGRES_DB=<db_name>
    POSTGRES_USER=<username>
    POSTGRES_PASSWORD=<password>

Execute this commands :

    docker-compose up -d --build
    docker-compose exec backend python api/manage.py createsuperuser

## Test

### Backend

    docker-compose exec backend python api/manage.py test movies

### Frontend
