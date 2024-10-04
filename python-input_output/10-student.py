#!/usr/bin/python3
""" Module for the Student class."""


class Student:
    """ A class to represent a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Returns a dictionary representation of the student's attributes
        for JSON serialization."""

        if attrs is None:
            return self.__dict__

        filtered_dict = {}

        if isinstance(attrs, list):
            for attr in attrs:
                if attr in self.__dict__:
                    filtered_dict[attr] = self.__dict__[attr]

        return filtered_dict
