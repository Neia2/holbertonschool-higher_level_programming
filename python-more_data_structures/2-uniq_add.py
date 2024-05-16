#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Add all unique integers in a list (each integer counted only once).

    Args:
        my_list (list of int): The list of integers.

    Returns:
        int: The sum of unique integers.
    """
    unique_integers = set(my_list)
    
    total_sum = sum(unique_integers)
    
    return total_sum
