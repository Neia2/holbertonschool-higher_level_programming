#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    Returns a new dictionary with all values multiplied by 2.

    :param a_dictionary: The original dictionary with integer values
    :return: A new dictionary with values multiplied by 2
    """
    new_dict = {key: value * 2 for key, value in a_dictionary.items()}
    return new_dict
