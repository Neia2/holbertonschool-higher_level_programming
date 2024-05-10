#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    Finds all multiples of 2 in a list.

    Args:
        my_list (list): List of integers.

    Returns:
        list: A new list with True or False indicating if the
        corresponding integer in the original list is a multiple of 2.
    """
    # Initialize the new list to store results
    result = []

    # Iterate over the original list
    for num in my_list:
        if num % 2 == 0:
            result.append(True)
        else:
            result.append(False)

    return result
