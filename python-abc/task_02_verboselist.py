#!/usr/bin/python3
"""Defining a class VerboseList that inherits from the built-in list class"""
class VerboseList(list):
    def append(self, item):
        """Add an item to the end of the list and print a notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        """Extend the list by appending elements from the iterable and print a notification."""
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, item):
        """Remove the first occurrence of an item in the list and print a notification."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=None):
        """Remove and return the item at the specified index or the last item if no index is specified."""
        if index is None:
            item = super().pop()
            print(f"Popped [{item}] from the list.")
        else:
            item = super().pop(index)
            print(f"Popped [{item}] from the list.")
        return item
