#!/usr/bin/python3
"""Module compiled with python3"""


class Student:
    """class student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance."""
        json_dict = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
        return json_dict
