#!/usr/bin/python3

"""A class BaseGeometry (based on 5-base_geometry.py)"""


class BaseGeometry:
    """Base class for geometry objects"""

    def area(self):
        """Public instance method that raises an exception"""
        raise Exception("area() is not implemented")
