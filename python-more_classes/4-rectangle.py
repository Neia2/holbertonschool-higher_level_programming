#!/usr/bin/python3
"""
This script contains utility functions for basic arithmetic operations.
"""


class Rectangle:
    """
    The Rectangle class represents a rectangle defined by its width
    and height.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """
        Gets the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        Gets the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
        int: The area of the rectangle.
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
        int or str: The perimeter of the rectangle if the width and
        height are not zero, otherwise returns "0".
        """

        if self.__width == 0 or self.__height == 0:
            return ("0")

        return (self.__width * 2 + self.__height * 2)

    def __str__(self):
        """
        Return a string representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        single_row = "#" * self.__width
        rows = map(lambda _: single_row, range(self.__height))
        return ("\n".join(rows))

    def __repr__(self):
        """
        Return a string representation of the rectangle instance.

        The string is formatted in a way that allows the creation of
        a new instance using eval(). For example, the returned string
        for a rectangle with width 4 and height 6 will be:
        'Rectangle(4, 6)'.

        Returns:
            str: A string that represents the rectangle object.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)
