
## TodoAPI

A Todo REST api written in Django Rest Framework

## Technologies used
* [Django](https://www.djangoproject.com/): The web framework for perfectionists with deadlines (Django builds better web apps with less code).
* [DRF](www.django-rest-framework.org/): A powerful and flexible toolkit for building Web APIs


## Installation
* If you wish to run your own build, first ensure you have python globally installed in your computer. If not, you can get python [here](https://www.python.org").
* Then, Git clone this repo to your PC
    ```bash
        $ git clone https://github.com/Abhishek9760/todolist_api
    ```

* #### Dependencies
    1. Cd into your the cloned repo as such:
        ```bash
            $ cd todolist_api
        ```
    2. Create and fire up your virtual environment:
        ```windows
            $ python -m venv env
            $ .\env\Scripts\activate
        ```
    3. Install the dependencies needed to run the app:
        ```bash
            $ pip install -r requirements.txt
        ```
    4. Make those migrations work
        ```bash
            $ python manage.py makemigrations
            $ python manage.py migrate
        ```

* #### Run It
    Fire up the server using this one simple command:
    ```bash
        $ python manage.py runserver
    ```
    You can now access the file api service on your browser by using
    ```
        http://localhost:8000/api/todo/
    ```


## Rest API Endpoints

1- GET - Get single todo by todo id - HTTP Response Code: **200**

`URL - /api/todos/<id>/`
```javascript
    HTTP/1.1 200
    Content-Type: application/json
    URL: /api/todos/1/

    {
        "id": 1,
        "timestamp": "2023-05-30T12:32:09.663208Z",
        "title": "Drink Water",
        "description": "Drink water from bottle haha",
        "due_date": "2023-05-31",
        "tags": [
            {
                "name": "hobby",
                "id": 1
            }
        ],
        "status": "OPEN"
    }
```
2- GET - Get all todos list - HTTP Response Code: **200**

`URL - /api/todos/`
```javascript
    HTTP/1.1 200
    Content-Type: application/json
    URL: /api/todos/
    
    [
        {
            "id": 16,
            "timestamp": "2023-05-31T07:02:48.361791Z",
            "title": "Do Exercise",
            "description": "Start yoga",
            "due_date": "2023-06-07",
            "tags": [
                {
                    "name": "hobby 4",
                    "id": 10
                },
                {
                    "name": "lifestyle",
                    "id": 11
                }
            ],
            "status": "OPEN"
        },
        ...
]
```

3- POST - Create a new todo - HTTP Response Code: **201**
```javascript
    Example request

    Content-Type: application/json
    URL: /api/todos/

    {
        "title": "New Todo",
        "description": "New Todo description",
        "due_date": "2023-07-31",
        "tags": [
            {
                "name": "latest"
            }
        ],
        "status": "OPEN"
    }

```
4- PUT - Update an item - HTTP Response Code: **200** 

`URL - /api/todos/<id>/`
```javascript
Example request

    Content-Type: application/json
 
    {
        "title": "Changed title",
        "description": "Drink water from bottle haha",
        "due_date": "2023-05-31",
        "tags": [
            {
                "name": "hobby"
            }
        ],
        "status": "OPEN"
    }
```

5- DELETE - Delete an item - HTTP Response Code: **204**
```javascript
    URL - /api/todos/<todo_id> 
```

