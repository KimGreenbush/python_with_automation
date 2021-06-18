# We're importing the connect function in order to establish a connection to our DB from within our
# application using pyodbc.
from pyodbc import connect

# We will be import "os" in order to pull environment variables
import os

# You should NEVER expose your credentials within your source code (and definitely never push the code
# if the credentials are exposed). There are many common solutions to this problem (e..g using environment
# variables, using properties files).
db_url= os.environ['db_url']
db_username= os.environ['db_username']
db_password= os.environ['db_password']
db_name= os.environ['db_name']

# This function will return a new connection to the database to the caller.
def get_connection():
    return connect(f"DRIVER={{PostgreSQL UNICODE}};SERVER={db_url};PORT=5432;DATABASE={db_name};UID={db_username};PWD={db_password};Trusted_Connection=no")