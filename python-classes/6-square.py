#!/usr/bin/python3
"defining a square class with size and position validation, area computation, accessors, and printing"

class Square:
    """A class representing a square with private size and position attributes."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the square with size and position.

        Args:
            size (int): The size of the square's sides.
            position (tuple): A tuple of two positive integers representing the square's position.
        """
        self.size = size           # Invokes the size setter
        self.position = position   # Invokes the position setter

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.

        Args:
            value (int): The size value to set.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square with validation.

        Args:
            value (tuple): A tuple of two positive integers.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square using the '#' character considering the position.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
            return

        # Print vertical offset
        for _ in range(self.__position[1]):
            print()

        # Print the square with horizontal offset
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
