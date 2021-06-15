# We had to import the JSONEncoder
from json import JSONEncoder

# id is a built-in function that is always available. We are shadowing id here, which is bad practice.
# I've only done this as proof of concept that id is a built-in function that is always visible.

id = 3
print('Print is also a built-in function')

enclosed_variable = "it's a string"

def enclosing_function():
    # By using this global keyword, we specify that we are referencing the "enclosed_variable" from
    # the outer scope
    global enclosed_variable
    enclosed_variable = 8

    local_variable = 'i am local'

    def enclosed_function():

        # We use the "nonlocal" keyword to refer to a variable from the enclosing scope. Please note
        # that your enclosing is not the global scope. If you use "nonlocal" when there is no binding
        # for the nonlocal variable, you will get a SyntaxError.
        nonlocal local_variable

    enclosed_function()

enclosing_function()

print(enclosed_variable)

# This function takes the sum of two numbers, but allows you to call this function two ways:
# 1. By just using the outer function and passing in two arguments (x and y)
# 2. By calling the outer function with just x and then calling the returned inner function with "z"
def sum(x, y=0):

    # Functions are objects (as everything in Python is an object), so we can actually define functions
    # within other functions like so:
    def fixed_sum(z):
        return x + z

    # First return scenario: A non-zero value was specified for y
    if y:
        return x + y
    # Second return scenario: Y is zero, so we return the inner function, which can later be called with
    # value we'd like to see added to x.
    else:
        return fixed_sum

# The first function call is to our "sum" function, to which we have to pass the positional argument "x".
# Because when we call "sum", we return a function called "inner_sum", our return value is actually a
# function that we can later invoke.
# print(sum(3, 8))
# print(sum(3)(8))

# This does exactly the same thing as the function call above, but this time we store the returned function
# before calling it.
# returned_function = sum(3)
# print(returned_function())

class User:

    # This is a class property that is in scope for the entirety of the class, which means that it can
    # be used within all of the methods defined here.
    unused_user_prop = True
    # Constructor for the user class
    def __init__(self, user_id, user_name, user_password, user_email, user_portfolio_list):
        # Any parameters that we defined within our parameter are only in scope for this method.
        self._user_id = user_id
        self._user_name = user_name
        self._user_password = user_password
        self._user_email = user_email
        self._user_portfolio_list = user_portfolio_list

# You guys want to create dummy data for the time being. As such, you decided to use some sort of container
# to do so. Your suggestions: list, set, dictionary (dict), tuple (you did not suggest this one, but it
# is on the curriculum)

# You guys have chosen to use a dict for your dummy users

# We're revisiting our dummy_users because we created a user model that we aren't currently using.
# We actually want to use this model because you've decided that each user that will have have a list
# of portfolios which we need access to

# You have retired the dict because you decided to add the password to the user model instead

# dummy_users = {'Tim The Enchanter': 'Monty Python', 'Killer Rabbit': 'grenade', 'hhg125': 'password'}

user1 = User(1, 'Tim The Enchanter', 'Monty Python', 'tim@revature.net', list())
user2 = User(2, 'Killer Rabbit', 'grenade', 'adorbs@not.com', list())
user3 = User(3, 'hhg125', 'password', 'hhg125@mp.com', list())

# Even though we've change the collection to dict, we still run into an issue because our user-defined type
# (which is called User) is not serializable. We must indicate that it should be serializable and how it
# should be serialized. In order to do so, we'll use the JSONEncoder class. We will make a custom encoder
# type that extends this class like so:

class UserEncoder(JSONEncoder):
    # In order to define how your type should be serialized, you should override the "default"
    # method:
    def default(self, user):
        if isinstance(user, User):
            return user.__dict__
        else:
            # If something should go wrong, just fall back on the default (parent) implementation
            # of this method
            return super().default(self, user)


dummy_users = {1:user1, 2:user2, 3:user3}