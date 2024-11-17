#!/usr/bin/python3
"""Create a class named CountedIterator that extends the built-in iterator """
class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)  # Create an iterator from the given iterable
        self.counter = 0  # Initialize the counter

    def __next__(self):
        # Increment counter and return the next item
        self.counter += 1
        return next(self.iterator)

    def get_count(self):
        # Return the count of iterated items
        return self.counter
