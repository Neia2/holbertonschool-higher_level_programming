#!/usr/bin/python3

"""
This script sums the command-line arguments passed to it,
excluding the script name.

It performs the following steps:
1. Counts the number of arguments provided.
2. If no arguments are provided, it prints "0".
3. If arguments are provided, it sums them (assuming all arguments
are integers).
4. Prints the result of the sum of the arguments.
"""

import sys


length = len(sys.argv) - 1
result = 0

if __name__ == "__main__":

    for argument in range(1, len(sys.argv)):

        result += int(sys.argv[argument])

    print("{}".format(result))