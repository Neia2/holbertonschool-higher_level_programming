#!/usr/bin/python3
"""Modulecompiled with python3"""
import json


def load_from_json_file(filename):
    """A function that creates an Object from a JSON file"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
