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

## Documentation

To understand:

* [Django](https://docs.djangoproject.com/en/3.0/)
* [Django Rest Framework](https://www.django-rest-framework.org/)
* [Tutorial](https://www.django-rest-framework.org/tutorial/1-serialization/) which was used in order to learn REST API
* [RESTful API guidelines](https://opensource.zalando.com/restful-api-guidelines/)

