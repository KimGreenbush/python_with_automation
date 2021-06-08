# Tim the Enchanter

# You guys want to create dummy data for the time being. As such, you decided to use some sort of container
# to do so. Your suggestions: list, set, dictionary (dict), tuple (you did not suggest this one, but it
# is on the curriculum)

# Creating a list of users. Please note that lists: support duplicates, allow you to access elements by
# their index, maintain their order

users = ['user1', 'user2', 'user1']
users_two = list()
users_three = list(users)

print(users)
print(users[0])

# Creating a set of users. Please note that sets: do not support duplicates, do not maintain order, do
# not allow access to their elements by index (e.g. set_of_users[0] raises a TypeError

# This creates a set with two elements
set_of_users = {'user1', 'user2'}
# This is an empty set. You CANNOT create an empty set using empty curly braces {}. You must use the
# set constructor.
empty_set = set()

# If I want to access the elements of my set, I can simply iterate over the set.

for user in set_of_users:
    print(user)

# Creating a dictionary of users. A dictionary (called a "dict" in Python) is an associative container
# which contains key-value pairs. Note that the equivalent of dict is a Map in some programming languages.

dictionary_of_users = {}
dictionary_of_users_two = dict()

# Please note that all keys within a dict must be unique but that values can be duplicated
dictionary_of_users_three = {1: 'password1', 'user2': 'password2', 1: 'another password'}

# We must use the key to access the underlying value
print(dictionary_of_users_three[1])

# Iterating over a dict:

# When we call the items() method, it returns a set-like object that we then iterate over
for key, value in dictionary_of_users_three.items():
    print(key, value)

# The input is a built-in function that you can use to prompt a user for input. Note that it returns
# that user input.

# username = input('Please enter username: ')
