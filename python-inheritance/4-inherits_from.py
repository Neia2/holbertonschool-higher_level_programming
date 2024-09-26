#!/usr/bin/python3

"""A function that returns True if the object is an instance of a class
  otherwise False"""


def inherits_from(obj, a_class):
    """A function to find out if inherits ditrect or indirect from another one"""
    return isinstance(obj, a_class)
