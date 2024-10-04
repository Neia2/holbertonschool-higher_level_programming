#!/usr/bin/python3
"""Module compiled with python3"""
import json


def save_to_json_file(my_obj, filename):
    """A function that writes an obj to a txt file, using a JSON repr"""

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
