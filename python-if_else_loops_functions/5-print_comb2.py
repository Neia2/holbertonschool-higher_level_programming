#!/usr/bin/python3

"""
Displays numbers from 00 to 99, separated by a comma and a space,
then displays “99” followed by a carriage return.
"""

numbers = ', '.join("{:02d}".format(i) for i in range(99))
print("{}, 99".format(numbers))