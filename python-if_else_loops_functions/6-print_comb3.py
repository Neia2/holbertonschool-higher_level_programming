#!/usr/bin/python3

"""
Prints all possible different combinations of two digits,
with the smallest combination first and separated by ', '.
"""
for i in range(10):
    for j in range(i + 1, 10):
        if i == 8 and j == 9:
            print(f"{i}{j}")
        else:
            print(f"{i}{j}, ", end="")
