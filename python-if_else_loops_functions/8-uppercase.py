#!/usr/bin/python3

"""
Prints a string in uppercase, converting lowercase letters.
"""
def uppercase(s):
    for char in s:
        if 'a' <= char <= 'z':
            char = chr(ord(char) - 32)
        print(char, end="")
    print()
