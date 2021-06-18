# We have to import the dummy users
import werkzeug

# Deprecated because we're not using dummy data anymore. Our data actually comes from the DB.
# from src.models.user import dummy_users as users

from src.models.user import *

# Let's import our custom JSONEncoder
from src.models.user import UserEncoder

# And let's import from json:
from json import dumps

# We also need to import the app (we called it flask_app in app.py) as we just want to reuse our existing
# instance of Flask
from src.app import flask_app

# In order to access the request body and head, we will import "request" from flask

from flask import request

# We want to import this built-in Flask collection of exceptions for easy use.
import werkzeug.exceptions

# We would like to add value to our debugging process. In essence, I would like to be able to present
# some deliverable to my team which shows a history of my efforts to trace issues in my project. This is
# essentially what is known as "logging".

import logging

# We are now going to import our user_service in order to call the functions which transform the data from our DB.
import src.service.user_service as u_service

# In order to configure our logger to write to a file (and change the logging level), we can do the
# following:

logging.basicConfig(filename='users.log', level=logging.INFO)

# We need to define a route to send all of our users to the client. In essence, we want to write the users
# to the response body so that they can be shipped back to the client.

@flask_app.route('/users', methods=['GET'])
def find_all():
    # This is not going to work; it will throw a TypeError because sets are not JSON seriliazable, meaning
    # that they cannot be written as JSON. As such, we will need to use a different type for our dummy users.
    # We have voted to use a dict.
    # my_json = jsonify(users)

    # We want to use the special JSONEncoder that we created not too long ago. Please note that we will
    # also want to import some functions from the json library.
    my_json = dumps(u_service.get_all_users(), cls=UserEncoder)
    return my_json

@flask_app.route('/user/<int:user_id>')
def find_by_id(user_id):
    logging.info('The user ID that the client passed back is: ' + str(user_id))
    # We need to check for the existence of the requested user ID
    if user_id in users:
        return dumps(users[user_id], cls=UserEncoder)
    # If the user does not exist in our system, let's return an error message to the client
    else:
        return 'No such user'

@flask_app.route('/user/new', methods=['POST'])
def add_new_user():
    client_json = request.get_json()
    # We are accessing the request body as JSON and logging it to our file
    logging.info(client_json)
    # Take the client data, validate it first, and then persisting
    new_user = User(4, client_json['name'], client_json['email'], client_json['password'], list())
    users[4] = new_user
    logging.info(users)
    return "User successfully created!"

@flask_app.route('/user/name_length')
def find_user_with_name_length():
    # In order to access a request parameter that has come back with the request, we can use "request",
    # which we imported earlier. We already have access to the request parameters via the "args" property.
    logging.info(request.args.get('length'))
    return 'Successfully retrieved reqeust parameter.'

# What if I want a default way of handling certain errors or exceptions which might occur in my application?
# I can define an "exception handler" which will be deferred to each time this exception or error occurs.

# We must specify what this errorhandler actually handles. In our case, we can use one of Flask's built-in
# exceptions.

@flask_app.errorhandler(werkzeug.exceptions.NotFound)
def handle_404(error):
    return '404 Not Found: No such resource exists on this server!', 404