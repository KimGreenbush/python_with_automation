# We can create our own custom exceptions and raise them.

# Please note that in order to create a child class, we must use the syntax that you see the below. The
# parent class is specified in the parentheses next to the class name. In this case, our parent class
# is Exception. Also note that if you are creating a custom exception type, you should extend Exception rather
# than BaseException as Exception is intended to be used for all non-exiting errors.

# Also note that all classes technically extend the object class. This is just implicit (e.g.
# class MyClass(object):

# Per someone's request (Jonathan's), we've made our custom exception a KeyError exception, which means
# that we can later handle this exception by catching a KeyError. Please note that this is optional for those
# of you that just prefer to just extend the Exception class.

class InvalidCredentialsError(KeyError):
    pass

try:
    raise InvalidCredentialsError()
except InvalidCredentialsError:
    print('I raised my own exception for demo purposes')

# The input is a built-in function that you can use to prompt a user for input. Note that it returns
# that user input.

username = input('Please enter username: ')
# # Pretend that this password has been hashed and that it's not stored as plain text
password = input('Please enter password: ')

# We want loop through our dict and compare our user's username and password to those contained within
# the dict

# Commented out for your reference
# for user_name, user_pass in dummy_users.items():
#     if username == user_name and password == user_pass:
#         print('You logged in successfully')

# # Please note that all objects in Python are truthy or falsy, which means that we can directly use them
# # as they will be resolved to a boolean value here:
# if 'not an empty string':
#     print('truthy')

# This line of code can cause an exception to be "raised". As such, we should do some exception handling.
# I say "should" because we are not required to handle this exception before running our script.

# Note that we need to return here to import the dummy users.

dummy_users[username]

# # We use "try" to denote that the code within this block might throw an exception.
try:
    if dummy_users[username] == password:
        print('Hello, ' + username)
    else:
        raise InvalidCredentialsError()
# We use the "except" keyword to course correct our application by handling the KeyError. In essence,
# we define what should happen when this exception type is raised.
except KeyError:
    print('Invalid login.')
# The finally block always executes. This means that if the KeyError is thrown, it executes. If the KeyError
# is not thrown, it STILL executes.
finally:
    print('I always execute.')

