# Assisi

Assisi is a platform for collecting requests first for Liberti Church's Easter
Outreach. The goal is to start with a simple API for writing "requests" to a
database and build lightweight clients on top of it. Examples could include
web forms, SMS, or voice.

This is an early prototype. Be ye warned.

## Local Setup

### 0. Install `virtualenv`

    $ pip install virtualenv

### 1. Setup a `virtualenv` in the project directory

    $ cd assisi
    $ virtualenv env

### 2. Activate the environment

    $ source env/bin/activate

You will need to do make sure your environment is active any time you wish to run the project. You can deactivate the environment by running `deactivate`.

### 3. Install python dependencies

    $ pip install -r requirements.txt

### 4. Create the `local_settings.py` file

    $ cp src/project/local_settings.py.template src/project/local_settings.py

This template will get you started right away with a SQLite database in your development environment.

### 5. Create the database and tables

    $ ./src/manage.py syncdb

Be sure to create a superuser when prompted.

### 6. Run the development server

    $ ./src/manage.py runserver

### 7. Visit http://127.0.0.1:8000/ and sign in

The data entry web application is at http://127.0.0.1:8000/admin/. The API endpoints are at http://127.0.0.1:8000/api/v1/.




