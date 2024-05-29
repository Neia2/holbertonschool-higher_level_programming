#!/usr/bin/python3
"""
Module 2-append_write
A module that contains a function to append a string at the end of a text.
"""


def append_write(filename="", text=""):
    """
    Append a string at the end of a text file (UTF8)

    Args:
        filename (str): The name of the file to append.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, 'a', encoding="utf-8") as file:
        nb_characters_added = file.write(text)
    return nb_characters_added
