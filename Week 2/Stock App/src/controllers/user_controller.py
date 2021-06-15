# We have to import the dummy users
from src.models.user import dummy_users as users

# Let's import our custom JSONEncoder
from src.models.user import UserEncoder

# And let's import from json:
from json import dumps

# We also need to import the app (we called it flask_app in app.py) as we just want to reuse our existing
# instance of Flask
from src.app import flask_app

from flask import jsonify

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
    my_json = dumps(users, cls=UserEncoder)
    return my_json