#!/usr/bin/python3
"""
Module 0-read_file
A module that contains a function to read and print a text file.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The name of the file to be read.

    Returns:
        None
    """
    with open(filename, encoding='utf-8') as f:
        text = f.read()
        print(text, end='')
