# We need to import our module for establishing a connection to the DB
from src.utils.dbconfigs import get_connection

# We need a function that pulls all of the users from our DB
def get_all_users():

    # We always want to start by getting our connection to our DB.
    try:
        db_connection = get_connection()
    # Now we want to use our DB connection to get a cursor. A cursor object represents a database cursor. We use
    # a database cursor to manage the context of an operation we're performing on our DB (e.g. an update, delete, insert)
        db_cursor = db_connection.cursor()
    # Now we can use our cursor to execute SQL statements against our DB. You can pass any valid SQL to execute.
        db_cursor.execute("select * from users")
    # Once you've execute your query, use your cursor to fetch all of the returned rows. Note that the rows are returned
    # as a collection of sequences (tuples)
        query_rows = db_cursor.fetchall()
    finally:
        # No matter what happens, please close the connection
        db_connection.close()

    return query_rows

def get_user_by_id():
    pass

# We've decided to pass the user back as a dictionary
def create_new_user(user):
    try:
        # Get a database connection
        db_connection = get_connection()
        db_cursor = db_connection.cursor()
        # The implementation which directly takes the client input and concatenates this in our SQL is bad practice as
        # it does not protect against SQL injection. SQL injection occurs when the client passes back valid SQL as input
        # in an attempt to access information from your DB or destroy data (e.g. 'drop table users; --'). We can protect
        # against SQL injection by using parameterization.
        db_cursor.execute("insert into users values(default, ?, ?, ?, ?)", (user['first_name'], user['last_name'], user['email'], user['password']))
        # We're not running in autocommit mode (purposely so), which means that we need to manually commit.
        db_connection.commit()
    finally:
        db_connection.close()