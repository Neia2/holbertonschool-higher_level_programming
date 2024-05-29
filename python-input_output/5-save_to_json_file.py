#!/usr/bin/python3
"""
Module 5-save_to_json_file
A module that contains a function to write an object using a JSON.
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Args:
        my_obj (object): The object to be serialized and written to the file.
        filename (str): The name of the file to be written.

    Returns:
        None
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
