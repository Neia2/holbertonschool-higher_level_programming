#!/usr/bin/python3
"""
This module defines a Rectangle class which models a rectangle shape
with width and height attributes. The class keeps track of the number
of instances created and deleted, allows for customization of the
symbol used for string representation, and includes methods to
calculate area and perimeter. Additionally, it provides methods to
compare rectangle sizes and create square instances.
"""

class Rectangle:
    """
    This class defines a rectangle with width and height attributes.
    It also keeps track of the number of instances created and deleted,
    and allows for customization of the symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle. Ensure it is an integer and >= 0."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle. Ensure it is an integer and >= 0."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """
        Return the perimeter of the rectangle, or 0 if width or height is 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Return a string representation of the rectangle with the character(s)
        stored in print_symbol.
        """
        if self.width == 0 or self.height == 0:
            return ""
        rect = ""
        for _ in range(self.height):
            rect += str(self.print_symbol) * self.width + "\n"
        return rect[:-1]

    def __repr__(self):
        """
        Return a string representation of the rectangle to recreate
        a new instance.
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Print a message when the instance is deleted and decrement the
        instance count.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Return the rectangle with the greater area, or rect_1 if they are equal.
        Raise a TypeError if rect_1 or rect_2 are not instances of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Return a new Rectangle instance with width == height == size.
        """
        return cls(size, size)
