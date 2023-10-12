#!/usr/bin/python3
"""Returns the JSON representation of a Python object."""
import json


def to_json_string(my_obj):
    """Return JSON representation of an object.

    Args:
        my_obj (str): the object in question.
    Returns:
        JSON representation of my_obj.
    """
    return json.dumps(my_obj)
