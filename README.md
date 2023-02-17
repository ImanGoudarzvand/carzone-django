
# Carzone

A Django used-car selling website 

## Screenshots

## Features
- User authentication
- Customized django admin panel 
- Dashboard for users
- Email sending
- Car search functionality
- Pagination

## Technologies
- Python 3.10
- Javascript
- Bootstrap
- Django 4
- HTML5
- CSS3
- CKEditor
- smtp
- PostgreSQL
- Docker

## Setup Using docker

Make sure you have the latest version of docker and docker compose on your machine.

https://docs.docker.com/desktop/<br>
https://docs.docker.com/compose/

    docker compose up -d
"-d" is for running in detatched mode.

### Populating the database:
    docker compose run api python manage.py loaddata project_dump.json

## Setup without docker

#### Install the Dependencies
First we use pipenv package to build a virtual environment for our project.

    pip install pipenv
#### To install the project dependencies:<br>
    pipenv install
#### To go to the virtual environment
    pipenv shell
Here we need to configure our <b>dev module</b> in settings folder to work outside the docker container:

    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'YOUR_DATABASE_NAME_HERE',
        'USER': 'YOUR_DATABASE_USER_HERE',
        'PASSWORD': 'YOUR_DATABASE_PASSWORD_HERE',
        'HOST': 'localhost',
                }
    }
    
In <b>common module</b> in settings folder:

    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 2525
    
    
    ALLOWED_HOSTS = []

#### Start the Server
    python manage.py runserver
If the porn is already taken try using another port

#### Populating the database
    python manage.py loaddata project_dump.json
