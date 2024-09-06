#!/usr/bin/python3

"""
Prints the ASCII alphabet in lowercase without a newline.
"""
for letter in range(97, 123):
    print('{}'.format(chr(letter)), end='')