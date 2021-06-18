# We need to import our user_dao so that we can access the functions
import src.dao.user_dao as udao
# Import the user model because we are formatting the DB data as user objects
from src.models.user import User

# This is a service function that transforms our user data from the DB to something more usable within our application
# (e.g. into User objects in this case)
def get_all_users():
    # We want to return a dictionary because they are easy to jsonify and flask likes dictionaries.
    user_dict = {}
    # Grab all of the user data from the user_dao's get_all_users function
    db_users = udao.get_all_users()
    # Perform the transformation so that these DB users are User objects
    for user in db_users:
        user_dict[user[0]] = User(user[0], user[1] + ' ' + user[2], user[4], user[3], list())

    return user_dict
