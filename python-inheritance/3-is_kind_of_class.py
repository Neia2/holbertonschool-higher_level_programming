#!/usr/bin/python3

"""
Module: 3-is_kind_of_class

This module defines a function is_kind_of_class that checks if an object is an instance of a class
inherited from a specified class.

"""

def is_kind_of_class(obj, a_class):
    """checks if obj is an instance of a class inherited from a_class
    Args
       obj: object
       a_class: class
    Return: True or False"""
    if isinstance(obj, a_class):
        return True
    return False
