#!/usr/bin/python3
"""
This module contains the function say_my_name.
The function say_my_name prints a message with the given first name and last name.
"""

def say_my_name(first_name, last_name=""):
    """
    Prints the full name in the format 'My name is <first name> <last name>'.

    Args:
        first_name (str): The first name.
        last_name (str): The last name. Default is an empty string.

    Raises:
        TypeError: If first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    print("My name is {} {}".format(first_name, last_name))