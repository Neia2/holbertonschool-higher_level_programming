#!/usr/bin/python3

"""
Module: 1-my_list

This module defines a class MyList, which is a subclass of the built-in list class.

"""

class MyList(list):
    """A custom list class that extends the built-in list."""

    def __init__(self):
        """Initializes a MyList object."""
        pass

    def print_sorted(self):
        """Prints the list sorted."""
        sorted_list = sorted(self)
        print(sorted_list)
