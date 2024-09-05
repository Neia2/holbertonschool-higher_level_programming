#!/usr/bin/python3

"""
Prints all numbers from 0 to 98 in decimal and hexadecimal format.
"""
for num in range(99 + 1):  # 0 to 99 inclusive
    print(f"{num} = 0x{num:x}")
