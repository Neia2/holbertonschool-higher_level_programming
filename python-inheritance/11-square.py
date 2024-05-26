#!/usr/bin/python3
"""
Module: 10-square

This module defines a class Square, which inherits from Rectangle.

"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """A class representing a square, a special case of rectangle with equal sides."""

    def __init__(self, size):
        """Initializes a square with a given size.

        Args:
            size (int): The size of one side of the square.
        """
        super().integer_validator('size', size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def __str__(self):
        """Returns a string representation of the square's dimensions."""
        return '[Square] {}/{}'.format(self.__size, self.__size)
