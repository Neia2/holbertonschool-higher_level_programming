#!/usr/bin/env python3

def uppercase(s):
    for char in s:
        if 97 <= ord(char) <= 122:  # Check if the character is lowercase
            print(chr(ord(char) - 32), end="")
        else:
            print(char, end="")
    print()
