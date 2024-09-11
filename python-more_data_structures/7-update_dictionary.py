#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    # Simply set the key to the new value
    # If the key already exists, its value will be replaced
    # If the key does not exist, it will be added
    a_dictionary[key] = value
    return a_dictionary

