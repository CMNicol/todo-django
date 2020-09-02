# Todo API

Django API to add, remove and retrieve to-do's from a PostgreSQL database.

## Docker implementation
Django server and PostgreSQL database set up in docker-compose.yml for local development.
See settings.py for the Django db configuration. 
See docker-compose.yml for the Docker db container configuration.

## Routes
* `GET /retrieve/`: Gets a list of  all todos in database, with some summary information.
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
```json
{
    "title": "Todo Numer 3",
    "description": "Description 3"
}
```
* `POST /remove/`: Removes a todo, with specified id, from the database.
```json
{
    "id": 1
}
```
