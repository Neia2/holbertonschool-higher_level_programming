#!/usr/bin/python3
"""
This module contains a function to print a square made of # characters.
"""

def print_square(size):
    """
    Prints a square made of # characters.

    Args:
        size (int): The size of the square's side.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.

    Example:
        >>> print_square(4)
        ####
        ####
        ####
        ####
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)

if __name__ == "__main__":
    import doctest
    doctest.testmod()