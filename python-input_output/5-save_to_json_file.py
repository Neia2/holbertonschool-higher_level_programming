#!/usr/bin/python3
import json
"""A function that writes an obj to a txt file, using a JSON representation"""


def save_to_json_file(my_obj, filename):

    with open(filename, "w") as outfile:
        json.dump(my_obj, outfile)
