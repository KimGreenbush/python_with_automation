from flask import Flask

# This is general Flask configuration. Note that you do not typically create several instances of
# the imported Flask class and that we are only doing it for today's demo.

# __name__ is a built-in variable which evaluates to the name of the current module. It is often used
# to determine whether the current script is being run on its own or being imported somewhere else. If
# a module is being directly run, __name__ evaluates to __main__.

flask_app = Flask(__name__)

# Let's create a hello world "endpoint". An endpoint simply exposes a resource to a client under a specific,
# unique identifier.

# This function declaration and the accompanying "decorator" allow us to define a resource that this server
# exposes to the client. A decorator takes in a function, adds some additional functionality, and returns
# said function.

# We have defined this resource as a "welcome" resource at the root of our application. If we simply navigate
# to http://localhost:5000/ this resource is returned to the client.

# Please note that the return value for a route must be formatted as either a: string, dictionary, tuple,
# Response instance.
@flask_app.route('/')
def hello_world():
    # Writing to the response body
    return 'Hello World'