#!/usr/bin/python3
"defining a square class with size validation, area computation, and accessors"

class Square:
    """A class representing a square with a private size attribute."""
    
    def __init__(self, size=0):
        """Initialize the square with a private size attribute, with validation."""
        self.size = size  # Use the setter for validation

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2
