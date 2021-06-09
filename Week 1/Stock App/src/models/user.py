class User:
    user_prop = True
    # Constructor for the user class
    def __init__(self, user_id, user_name, user_password, user_email, user_portfolio_list):
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

dummy_users = {user1, user2, user3}