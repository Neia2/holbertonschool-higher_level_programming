#!/usr/bin/python3
import json
"""Module for JSON representation of an object.

This module contains a function that converts a Python object to
its JSON string representation.
"""


def to_json_string(my_obj):
    """Converts an object to its JSON string representation.

    Args:
        my_obj (object): The Python object to be converted to a JSON string.

    Returns:
        str: The JSON string representation of the given object.

    """
    return json.dumps(my_obj)
