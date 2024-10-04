#!/usr/bin/python3
"""Module compiled with python3"""


def class_to_json(obj):
    """returning the dictionary description with simple data structure"""
    return obj.__dict__
