#!/usr/bin/python3
"""
This module defines a Rectangle class.

The Rectangle class defines a rectangle by its width and height.
It includes methods to calculate the area and perimeter of the rectangle.
Additionally, it provides a string representation of the rectangle using the '#' character.
"""

class Rectangle:
    """
    A class that defines a rectangle by its width and height.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

    Methods:
        area: Returns the area of the rectangle.
        perimeter: Returns the perimeter of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle with optional width and height.

        Args:
            width (int): The width of the rectangle. Default is 0.
            height (int): The height of the rectangle. Default is 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns a string representation of the rectangle with the character #."""
        if self.width == 0 or self.height == 0:
            return ""
        rectangle_str = "\n".join(["#" * self.width for _ in range(self.height)])
        return rectangle_str

    def __repr__(self):
        """Returns a string representation of the rectangle for debugging purposes."""
        return f"<Rectangle(width={self.width}, height={self.height})>"
