#!/usr/bin/python3
def add_integer(a, b=98):
    """Adds two integers or integers casted from floats.

    Args:
        a: The first value, must be an integer or float.
        b: The second value, must be an integer or float, default is 98.

    Returns:
        The integer sum of a and b.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    
    return a + b
