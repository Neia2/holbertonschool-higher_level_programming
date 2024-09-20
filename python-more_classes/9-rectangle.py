#!/usr/bin/python3
"""
This script contains utility functions for basic arithmetic operations.
"""


class Rectangle:
    """
    The Rectangle class represents a rectangle defined by its width
    and height.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Gets the width of the rectangle.
        Used as symbol for string representation
        Can be any type
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

        single_row = str(self.print_symbol * self.__width)
        rows = list(map(lambda _: single_row, range(self.__height)))
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        This module defines a Rectangle class and provides
        a static method to compare
        two rectangle instances based on their areas.

        The class includes methods to determine the area of each rectangle
        and a static method that returns the rectangle with the larger
        or equal area.
        If the two rectangles have the same area, the first rectangle
        is returned.

        Usage:
            - Create instances of the Rectangle class.
            - Use the `bigger_or_equal` static method to
            compare two rectangle instances.

        Exceptions:
            - Raises TypeError if the provided inputs are not instances of the
            Rectangle class.
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1

        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        This module defines a Rectangle class and provides
        a class method to create a square instance.

        The class includes methods to determine the area of the square
        and a class method that
        """

        if size < 0:
            size = 0

        return cls(size, size)

    def __del__(self):
        """
        Print a message when an instance of Rectangle is deleted.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
