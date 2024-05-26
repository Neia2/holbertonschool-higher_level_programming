#!/usr/bin/python3
"""
Module: 6-base_geometry

This module defines a class BaseGeometry that serves as a base class for geometric shapes.

"""

class BaseGeometry:
    """Base geometry class"""

    def area(self):
        """Calculate the area of the geometric shape.
        
        This method raises an Exception since it should be implemented by subclasses.
        """
        raise Exception('area() is not implemented')
