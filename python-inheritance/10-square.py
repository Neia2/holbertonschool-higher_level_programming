#!/usr/bin/python3

"""
Module: 10-square

This module defines a class Square, which inherits from Rectangle.

"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """square class"""

    def __init__(self, size):
        """initializer
        Args:
           size: size of side of square
        """
        super().integer_validator('size', size)
        Rectangle.__init__(self, size, size)
