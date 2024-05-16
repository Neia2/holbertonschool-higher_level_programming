#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Replace all occurrences of an element in a list with another element.

    Args:
        my_list (list): The original list.
        search: The element to be replaced in the list.
        replace: The new element to replace the search element.

    Returns:
        list: A new list with the search element replaced by the replace element.
    """
    # Criação de uma nova lista com os valores substituídos
    new_list = [
        replace if element == search else element
        for element in my_list
    ]
    return new_list
