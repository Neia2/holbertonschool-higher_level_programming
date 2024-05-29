#!/usr/bin/python3
"""Module compiled with python3"""


import json

def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.
    
    Args:
        data (dict): The Python dictionary to serialize.
        filename (str): The name of the file to save the JSON data.
    """
    # Open the file in write mode ('w')
    with open(filename, 'w') as file:
        # Serialize data to JSON and write it to the file
        json.dump(data, file)

def load_and_deserialize(filename):
    """
    Load and deserialize a JSON file to a Python dictionary.
    
    Args:
        filename (str): The name of the JSON file to read.
        
    Returns:
        dict: The deserialized Python dictionary.
    """
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
