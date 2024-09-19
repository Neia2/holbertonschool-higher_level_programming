#!/usr/bin/python3
"defining a square class with size validation and area computation"

class Square:
    
    def __init__(self, size=0):
        """Initialize the square with a private size attribute, with validation."""
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2
