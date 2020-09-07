# Todo API

Django API to add, remove and retrieve todo's from a PostgreSQL database.

## Docker Implementation
Django server and PostgreSQL database set up in docker-compose.yml for local development.
See settings.py for the Django db configuration. 
See docker-compose.yml for the Docker db container configuration.
As per the compose.yml file, the Django app is mapped to port 8000, and the database to port 5432.

## To Run In Docker
* Open a terminal and `cd` to the project root
* Run `docker-compose build` to build the django-api service from the Dockerfile
* Run `docker-compose run django-api python manage.py migrate` to run the database migrations and setup the database.
* Run `docker-compose up` to run the container.

## Routes

In the default project configuration, these routes will be accessible at `http://127.0.0.1:8000/<route>/`

* `GET /retrieve/`: Gets a list of  all todos in database, with some summary information. Response format:
```json
{
    "number of todos": 2,
    "number complete": 1,
    "number incomplete": 1,
    "todos": [
        {
            "id": 1,
            "title": "Todo Number 1",
            "description": "Description 1",
            "status": true
        },
        {
            "id": 2,
            "title": "Todo Number 2",
            "description": "Description",
            "status": false
        },
    ]
}
```
* `POST /add/`: Adds a new todo to the database with title and description.
Request format:
```json
{
    "title": "Todo Numer 3",
    "description": "Description 3"
}
```
* `POST /remove/`: Removes a todo, with specified id, from the database. Request format:
```json
{
    "id": 1
}
```
* `POST /edit/`: Edit a todo. Specifying id, and any fields to be updated. Request format:
```json
{
    "id": 1,
    "<field to edit>": "blah blah",
    "<another field to edit>": "blah blah"
}
```
