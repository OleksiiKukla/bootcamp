


# Start app

Create .env file from .env_example with your credentials.

Migrate database:

    python manage.py migrate

Start app command:

    python manage.py runserver

Swager:

    http://127.0.0.1:8000/api/docs/

# Start app with Docker
Create .env file from .env_example with your credentials.

    sudo docker-compose build
    sudo docker-compose up
    docker exec -it bootcamp-web-1 bash
    python manage.py migrate


