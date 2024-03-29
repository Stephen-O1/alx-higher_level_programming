#!/usr/bin/python3
"""
Module 6-load_from_json_file

Contains function that creates a python obj from JSOn file
"""

def load_from_json_file(filename):
    """Creates a Python obj from JSON file
    Args:
        filename: file
    """
    import json

    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
