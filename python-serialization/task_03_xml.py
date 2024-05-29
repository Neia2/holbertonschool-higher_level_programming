#!/usr/bin/python3
"""Module compiled with python3"""


import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")
    
    for key, value in dictionary.items():
        child = ET.Element(key)
        child.text = str(value)
        root.append(child)
    
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)

def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text
    
    return dictionary
