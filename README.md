# Courses Application

This project is created in order to understand Simple REST API by using Django and Django Rest Framework. 
There are POST and GET requests for <b> courses list </b> with GET and DELETE fro <b> course detail </b>.

## Installation

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 
*(Commands are written for Windows.)*

### Requirments

Frist of all, get virtual environment and activate it:
```
python -m venv env
env\Scripts\activate
```

Now that you're inside a virtual environment, install project's package requirements:

```
pip install django
pip install djangorestframework
pip install psycopg2
```

## Getting started

There is overview on how it works:
```
cd courses_app
python manage.py runserver
```
Go to localhost:
* for courses list to http://127.0.0.1:8000/course/
* for course detail to http://127.0.0.1:8000/course/ {course id}

## Running the tests

## Documentation

HOST http://127.0.0.1:8000/course/

### Course List

Course List is a simple API allowing consumers to view courses.

#### Courses Collection [/course]

#### List All Courses [GET]

+ Response 200 *(application/json)*

```
    {
        "name": "Bakery courses",
        "description": "How to make cakes and pies!",
        "category": 3,
        "logo": "img.jpg",
        "contacts": [
            {
                "contact_type": 1,
                "value": "0999999999"
            }
        ],
        "branches": [
            {
                "latitude": "42.874622",
                "longtitude": "74.569763",
                "adress": "7th microdistrict"
            }
        ]
    }
  
```

#### Create a New Question [POST]

+ Request *(application/json)*

```
{
    "name": "Test",
    "description": "Testing",
    "category": 1,
    "logo": "logo.jpg",
    "contacts": [
            {
                "contact_type": 1,
                "value": "01111111"
            }
     ],
    "branches": [
            {
                "latitude": "Test",
                "longtitude": "Test",
                "adress": "Test"
            }
    ]
}
```

+ Response 201 (application/json)

    + Headers

            Location: /course/1

    + Body
```
        {
                "name": "Testing",
                "description": "test",
                "category": 2,
                "logo": "test",
                "contacts": [
                    {
                        "contact_type": 1,
                        "value": "01111111"
                    }
                ],
                "branches": [
                    {
                        "latitude": "Test",
                        "longtitude": "Test",
                        "adress": "Test"
                    }
                ]
            }
```
### Course [/course/{course_id}]

+ Parameters
    + courseid (number) - ID of the Course in the form of an integer
    
## Deployment

## Built With

* [Django](https://docs.djangoproject.com/en/3.0/)
* [Django Rest Framework](https://www.django-rest-framework.org/)
* [Tutorial](https://www.django-rest-framework.org/tutorial/1-serialization/) which was used in order to learn REST API
* [RESTful API guidelines](https://opensource.zalando.com/restful-api-guidelines/)

## Versioning

There is no other versions

## Authors

* <b>Nazgul Ismailova</b> - *initial work* - [ismailovan](https://github.com/ismailovan)
