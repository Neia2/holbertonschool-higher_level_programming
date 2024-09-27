#!/usr/bin/python3
"""Defining a class Rectangle that inherits from rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square that inherits from Rectangle """

    def __init__(self, size):
        """ Initialize a square with a single size """
        self.integer_validator("size", size)
        self.__size = size

        super().__init__(size, size)

    def __str__(self):
        """ Return the square description """
        return f"[Square] {self.__size}/{self.__size}"
