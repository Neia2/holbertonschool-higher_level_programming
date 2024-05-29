#!/usr/bin/python3
"""
Module 1-write_file
A module that contains a function to write a string to a text file (UTF8).
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8).

    Args:
        filename (str): The name of the file to be written.
        text (str): The string to write to the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, mode='w', encoding='utf-8') as a_file:
        num_characters = a_file.write(text)
    return num_characters
