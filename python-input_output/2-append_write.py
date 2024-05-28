#!/usr/bin/python3
def append_write(filename="", text=""):
    """
    Append a string at the end of a text file (UTF8) and return the number of characters added.

    Args:
        filename (str): The name of the file to which the text will be appended.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, 'a', encoding="utf-8") as file:
        file.write(text)
        nb_characters_added = len(text)
    return nb_characters_added
