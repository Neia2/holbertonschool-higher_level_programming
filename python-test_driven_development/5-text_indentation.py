#!/usr/bin/python3
"""
This module provides a function `text_indentation` that prints a given text with
two new lines after each of these characters: '.', '?', and ':'.
"""

def text_indentation(text):
    """Prints text with 2 new lines after each '.', '?' or ':'
    
    Args:
        text (str): The text to be processed.
        
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    
    begin = 0
    for i, c in enumerate(text):
        if c in '.?:':
            print(text[begin: i + 1].strip())
            print()
            begin = i + 1
    if begin < len(text):
        print(text[begin:].strip())
        print()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
