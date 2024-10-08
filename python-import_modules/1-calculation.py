#!/usr/bin/python3
"""
This module imports basic arithmetic functions (add, sub, mul, div)
and performs operations on two integers.
"""

from calculator_1 import add, sub, mul, div

a = 10
b = 5


if __name__ == "__main__":
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))