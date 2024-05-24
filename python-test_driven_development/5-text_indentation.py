#!/usr/bin/python3
def text_indentation(text):
    """
This module provides a function `text_indentation` that prints a given text with
two new lines after each of these characters: '.', '?', and ':'.
"""
    begin = 0
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    for i, c in enumerate(text):
        if c in '.?:':
            print(text[begin: i + 1].strip() + '\n')
            begin = i + 1
    if begin < len(text):
        print(text[begin:].strip(), end="")

if __name__ == "__main__":
    import doctest
    doctest.testmod()