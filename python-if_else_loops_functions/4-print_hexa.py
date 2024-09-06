#!/usr/bin/python3

"""
This script is executed using the Python 3 interpreter.

It prints numbers from 0 to 98 alongside their hexadecimal
representation. The numbers are printed in the format:
<number> = 0x<hexadecimal>, with each pair on a new line.
"""

for i in range(0, 99):
    print("{} = 0x{:x}".format(i, i))