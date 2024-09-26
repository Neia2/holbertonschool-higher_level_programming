#!/usr/bin/python3

"""A class BaseGeometry"""


class BaseGeometry:
    """Base class for geometry objects"""

    def area(self):
        """Public instance method that raises an exception"""
        raise Exception("area() is not implemented")
