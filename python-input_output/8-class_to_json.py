#!/usr/bin/python3
"""Module compiled with python3"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure

    Args:
        obj: An instance of a class.

    Returns:
        dict: A dictionary representation of the object.
    """
    return obj.__dict__
