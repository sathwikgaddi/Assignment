##Overview

Two models User and ActivityPeriod models are created

A custom management command `$ python manage.py populateUsers` is written to populate the dummy data into the database in the given format

An api is written to serve the data in the given json format




##Installations required

Install django

`$pip install django`

Install requests

`$pip install requests`

Install django rest framework

`$pip install djangorestframework`

Install Faker

`$pip install Faker`

Install django-populate

`$pip install django-populate`

##Custom management command

Run  `$ python manage.py populateUsers` where populateUsers is a custom command which populates the data into the database.
Faker is used to get dummy data

api is created to serve the data in the given json format
`$python manage.py  runserver` 

Open `localhost:8000/users` to view the json data 

Its is deployed in heroku `http://pydjass.herokuapp.com/users/` but there is some Programming error.
