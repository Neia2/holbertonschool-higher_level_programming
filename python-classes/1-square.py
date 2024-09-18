#!/usr/bin/python3

class Square:
    """A class representing a square with a private size attribute."""
    
    def __init__(self, size):
        self.__size = size

my_square = Square(3)
