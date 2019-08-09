# [BLOGGING HOOD](https://init-blog.herokuapp.com/)

## Author

By [James Kirwa](https://github.com/Jameskirwa/Blogging-Hood)

## Description

- This website allows a user to view and add blogs.The user can also vote on a blog and commennt on it.

## BDD

Get the specifications by clicking [here](/specs.md)

### Requirements

- You need to have python 3.6 installed in your computer.
- You must have a working internet service.

#### - Setup and Instalations

- You first need to clone the application by runing the following command on the terminal:
`$ git clone https://jameskirwa.github.io/Blogging-Hood/` then install [Postgres](https://www.postgresql.org/download/) to your computer.

- Run the following commands in the same terminal:
`$ python3.6 -m venv --without-pip virtual`
`$ source virtual/bin/activate`
then run this command to install pip addons`$ curl https://bootstrap.pypa.io/get-pip.py | python`

 Run the following in the start.sh file to prepare your internet environment to run.
zsh or bash
$ export DATABASE_URL='postgresql+psycopg2://your username:your password@localhost/your db'
$ export SECRET_KEY='Your secret key'

Run this commands to be able to migrate your database to application.
zsh or bash
$ python manage.py db init
$ python manage.py db migrate -m "initial migration"
$ python manage.py db upgrade
In the same terminal type use this command to run your application:
`$ python3 manage.py server` then open the browser at `http://localhost:5000/`

## Known bugs

SQLAlchemy errors, automatic sign out has a short time span

## Technologies used

    - Python 3.6
    - HTML
    - Bootstrap 4
    - JavaScript
    - Heroku
    - Postgresql

### Contact details

You can contact me at jameskirwa34@gmail.com for any feedback.

### License

This is a [MIT licensed](/LICENSE) application.

Copyright (c) **James Kirwa**
