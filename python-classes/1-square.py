#!/usr/bin/python3
"defining a square class"

class Square:
    """A class representing a square with a private size attribute."""
    
    def __init__(self, size):
        """Initialize the square with a private size attribute."""
        self.__size = size

my_square = Square(3)
