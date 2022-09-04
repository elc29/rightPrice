from random import randint
from interactionModule import *

"""
--- rightPrice ---
First step : the program generate a random int
Second step : the goal of the user is to find the right price
Third step : each time that the user has a false value, its reachable final score (maximum value : 10)
decreased and the program say if the price is bigger or smaller than the user's price.
"""

# First step : the program generate a random int
theRightPrice = randint(0, 1000)

# Second step : the goal of the user is to find the right price
userPrice = int(input('Which price do you think of ?\n'))

# Creating a variable for the initial user's score
score = 10

# Third step : each time that the user has a false value, its reachable final score (maximum value : 10) decreased.
while userPrice != theRightPrice and score != 0:
    # the program say if the price is bigger or smaller than the user's price
    print(compare_value(userPrice, theRightPrice))

    score = score - 1
    userPrice = int(input('Which price do you think of ?\n'))

print(final_msg(score))
