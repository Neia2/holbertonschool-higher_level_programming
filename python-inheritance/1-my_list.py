#!/usr/bin/python3
"""A class MyList that inherits from list"""


class MyList(list):
    def print_sorted(self):
        """printing a sorted list"""
        print(sorted(self))
