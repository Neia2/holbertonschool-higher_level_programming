#!/usr/bin/python3

"""
Prints the ASCII alphabet in lowercase except for the letters 'q' and 'e'.
"""
for letter in range(ord('a'), ord('z') + 1):
    if chr(letter) not in ('q', 'e'):
        print(chr(letter), end="")
