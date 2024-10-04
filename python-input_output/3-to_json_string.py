#!/usr/bin/python3
"""Module compiled with python3"""
import json


def to_json_string(my_obj):
    """A function that converts a Python object to its JSON str repr"""
    return json.dumps(my_obj)
