#!/usr/bin/python3

for i in range(10):
    """
    Loop through each digit from 0 to 9.
    """
    for j in range(i + 1, 10):
        """
        Loop through the next digits starting from i+1 to avoid repeating
        combinations in different orders (e.g., 01 and 10).
        """
        if i == 8 and j == 9:
            print("{}{}".format(i, j))
        else:
            print("{}{}, ".format(i, j), end="")