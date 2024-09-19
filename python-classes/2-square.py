#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        """Initialize the square with a private size attribute, with validation."""
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
