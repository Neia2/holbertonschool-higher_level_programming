#!/usr/bin/python3
class Rectangle:
    """
    A class used to represent a Rectangle

    ...

    Attributes
    ----------
    width : int
        width of the rectangle (default is 0)
    height : int
        height of the rectangle (default is 0)
    number_of_instances : int
        number of instances of the Rectangle class

    Methods
    -------
    area()
        Returns the area of the rectangle
    perimeter()
        Returns the perimeter of the rectangle
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Constructs all the necessary attributes for the rectangle object.

        Parameters
        ----------
        width : int, optional
            The width of the rectangle (default is 0)
        height : int, optional
            The height of the rectangle (default is 0)
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns a string representation of the rectangle using the character #"""
        if self.width == 0 or self.height == 0:
            return ""
        rect = ""
        for _ in range(self.height):
            rect += "#" * self.width + "\n"
        return rect.rstrip()

    def __repr__(self):
        """Returns a string representation of the rectangle for recreation"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Prints a message upon deletion of an instance and decrements the instance count"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
