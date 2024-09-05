#!/usr/bin/python3

"""
Imports the random module, which contains functions to generate random numbers.
"""
import random

"""
Generates a random integer between -10 and 10 (inclusive)
and assigns it to the variable 'number'.
"""
number = random.randint(-10, 10)

"""
Checks if the number is equal to 0, less than 0, or greater than 0.
"""
if number == 0:
    print(f"{number} is zero")
elif number < 0:
    print(f"{number} is negative")
else:
    print(f"{number} is positive")
