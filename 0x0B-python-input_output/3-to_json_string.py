#!/usr/bin/python3
"""Contain a function that returns the json representation of a string."""
import json


def to_json_string(my_obj):
    """Return JSON representation of an object.

    Args:
        my_obj (str): the object in question.
    Returns:
        JSON representation of my_obj.
    """
    return json.dumps(my_obj)
