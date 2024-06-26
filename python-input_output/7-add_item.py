#!/usr/bin/python3
"""
Module 7-add_item
A script that adds all arguments to a Python list and saves them to a file.
"""

import sys
import os


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

if os.path.exists(filename) and os.path.getsize(filename) > 0:
    try:
        items = load_from_json_file(filename)
    except json.JSONDecodeError:
        items = []
else:
    items = []

items.extend(sys.argv[1:])
save_to_json_file(items, filename)
