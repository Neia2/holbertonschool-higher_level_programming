#!/usr/bin/python3
"""A class MyList that inherits from list"""


class MyList(list):
    def print_sorted(self):
        """Printing a sorted list without modifying the original"""
        print(sorted(self))
