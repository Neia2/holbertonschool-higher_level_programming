#!/usr/bin/python3
"""A function that writes a string to a text file (UTF8) and returns the
 number of characters written"""


def append_write(filename="", text=""):
    """appending a text to a file"""
    with open('file_append.txt', mode="a", encoding="utf-8") as f:
        return f.write(text)
