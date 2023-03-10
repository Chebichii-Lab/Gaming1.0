# Gaming

## Author
Natasha Serem

## Description
This is a simple gaming platform where a user can create an account, log in, upload a game via a game image, view existing games that have been uploaded by other users, rate the games and click a link that directs the users to the actual game.

## Set up and Installations
To get the code, clone the repository https://github.com/Chebichii-Lab/Gaming1.0.git and run the following commands;

    $ cd Gaming1.0
    $ pip install -r requirements.txt

### Install and activate virtual environment
    $ python3.8 -m venv virtual 
    $ source virtual/bin/activate

### Create Database
    $ psql
    $ CREATE DATABASE (name_of_database);

### Running the application
    $ python3.8 manage.py runserver (or python3 manage.py runserver.py)

Then once you are done, open the browser with the local host; 127.0.0.1:8000

## Dependencies
1. Python 3.10.6
2. Django 4.0
3. Virtual Environment

## Technologies Used
1. Python
2. Django
3. HTML
4. CSS
5. Postgresql

