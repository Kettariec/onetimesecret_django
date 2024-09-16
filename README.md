<h2 align="center">One-time note service</h2>

#### Service of one-time secret notes like a onetimesecret.com
#### Write a secret, determine the lifetime of the secret and receive a one-time key. When the secret's lifetime expires or is read, the secret is deleted. All secrets are stored in encrypted form and no one has access to them!


<!-- USAGE EXAMPLES -->
## Usage

Before running the web application, create a database, create and apply migrations, install the necessary packages from the pyproject.toml file and populate the .env file with .env.example. To run, use the command "python manage.py runserver".


## Docker 
Create Docker images and containers using commands: "docker-compose build" and "docker-compose up".


## Project structure

config/

    celery.py - celery file
    settings.py - application settings
    urls.py - routing file

onetimesecret/

    migrations/
        directory with migrations
    templates/
        directory with html templates
    admin.py - admin settings
    forms.py - application forms
    models.py - application models
    services.py - service functions
    tasks.py = periodic task
    tests.py - application tests
    urls.py - application routing file
    views.py - controllers

static/ 

    css/
        directory with css files
    js/
        directory with js files
    logo.png - project logo

.gitignore - Git file.

Dockerfile <br>
docker-compose.yaml - Docker files.

env.example - example of filling environment variables.

manage.py - web application entry point.

pyproject.toml - requirements for the project.

poetry.lock - poetry file.


<!-- CONTACT -->
## Contact
kettariec@gmail.com

https://github.com/Kettariec/onetimesecret_django