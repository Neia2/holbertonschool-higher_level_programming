#!/usr/bin/python3
def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    # Use a temporary variable to build the result
    result = ""
    skip_space = True  # To skip leading spaces after special characters
    
    for char in text:
        result += char
        if char in ".:?":
            result += "\n\n"
            skip_space = True  # Skip any leading spaces in the next line
        elif skip_space and char == " ":
            result = result[:-1]  # Remove the extra space added
        else:
            skip_space = False  # Reset skip space
        
    print(result, end="")
