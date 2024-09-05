#!/usr/bin/python3

"""
Imports the random module, which contains functions to generate random numbers.
"""
import random

"""
Generates a random integer between -10000 and 10000 (inclusive)
and assigns it to the variable 'number'.
"""
number = random.randint(-10000, 10000)

"""
Calculates the last digit of the number and prints it along with additional messages
based on its value.
"""
last_digit = number % 10

# Handle negative last digit case
if number < 0:
    last_digit *= -1

print(f"Last digit of {number} is {last_digit}", end="")

if last_digit > 5:
    print(" and is greater than 5")
elif last_digit == 0:
    print(" and is 0")
else:
    print(" and is less than 6 and not 0")
