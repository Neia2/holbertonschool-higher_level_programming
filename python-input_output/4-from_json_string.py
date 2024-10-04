#!/usr/bin/python3
import json
"""A function that returns an object represented by a json string"""


def from_json_string(my_str):
    return json.loads(my_str)
