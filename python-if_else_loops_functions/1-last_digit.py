#!/usr/bin/python3

"""
Import the random module, which contains functions to generate random numbers.
"""
import random

"""
Generate a random integer between -10000 and 10000 (inclusive)
and assign it to the variable 'number'.
"""
number = random.randint(-10000, 10000)

"""
Calculate the last digit of 'number'
"""
ld = number % 10

"""
Adjust the last digit for negative numbers
"""
if number < 0:
    ld = number * -1 % 10 * -1

"""
Check if the last digit is 0
"""
if ld == 0:
    print(f"Last digit of {number} is {ld} and is 0")
    """
    Check if the last digit is less than 6 and not 0
    """
elif ld < 6:
    print(f"Last digit of {number} is {ld} and is less than 6 and not 0")

    """
    Check if the last digit is greater than 5
    """
else:
    print(f"Last digit of {number} is {ld} and is greater than 5")