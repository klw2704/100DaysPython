# Random Module
    # python uses the mersenne twister for its random number generator

from os import stat_result
import random

# use randint() for random integers, provide two numbers and python will generate a random number between and including the two 

random_integer = random.randint(1, 10)
print(random_integer)


# using other modules
    # you caqn create another .py document with a module in it, for example my_module.py, import it and then print(my_module.py) - this is how the random module works


# use random.random() to get a random float
random_float = random.random()
print(random_float)

# how to create a random decimal number between 0 and 5?
    # times the random_float variable by a number, in this instance 5


# Understanding the offset and appending items to lists 
# lists are a set of square brackets with items stored inside
    # can be mixed, strings with numbers, booleans etc

states_of_america = ["Delaware", "Pensylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

#print(states_of_america)

print(states_of_america[0]) # - positive index
print(states_of_america[-1]) # - negative index

# to change something in the list
states_of_america[1] = "Pennsylvania"
#print(states_of_america)


# adding a single item to the list
# states_of_america.append("another state")

# extending the list, adding multiple items
# states_of_america.extend(["and another", "another"])


# Index Errors and Working with Nested Lists

num_of_states = len(states_of_america)
print(num_of_states)
print(states_of_america[num_of_states - 1]) # prints how many items are in the list, but it is offset so..

#lists within lists
#dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)