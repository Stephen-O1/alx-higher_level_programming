#!/usr/bin/python3
"""
Functions that returns JSON representations of object string
"""

def to_json_string(my_obj):
    import json

    return json.dumps(my_obj)
