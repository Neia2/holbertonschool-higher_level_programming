#!/usr/bin/python3
"""Reading a file"""


def read_file(filename="my_file_0.txt"):
    """A function that reads a text file and prints it to stdout"""
    with open(filename, 'r', encoding="utf-8") as file:
        print(file.read())
