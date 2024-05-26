#!/usr/bin/python3

"""
Module: 2-is_same_class

This module defines a function is_same_class that checks if an object is exactly an instance
of a specified class.

"""

def is_same_class(obj, a_class):
    """checks if object is exactly an instance of a_class
    Args
       obj: object
       a_class: class
    """
    return type(obj) == a_class
