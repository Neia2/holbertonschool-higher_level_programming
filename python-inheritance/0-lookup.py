#!/usr/bin/python3
"""
Module: 0-lookup

This module provides a function to retrieve the list of attributes and methods of an object.

"""

def lookup(obj):
    """Returns the list of attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list containing the names of attributes and methods of the object.
    """
    return dir(obj)
