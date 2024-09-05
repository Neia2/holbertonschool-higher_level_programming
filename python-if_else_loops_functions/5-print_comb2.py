#!/usr/bin/python3

"""
Prints all numbers from 00 to 99, separated by ', ' with proper formatting.
"""
for num in range(100):
    if num < 99:
        print(f"{num:02d}, ", end="")
    else:
        print(f"{num:02d}")
