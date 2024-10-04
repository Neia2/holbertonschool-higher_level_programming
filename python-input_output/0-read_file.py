#!/usr/bin/python3
"""
Module 0-read_file
A module that contains a function to read and print a text file.
"""


def read_file(filename="my_file_0.txt"):
    """Reads a text file and prints it to stdout"""
    with open(filename, 'r', encoding="utf-8") as f:
        print("{}".format(f.read()), end="")
