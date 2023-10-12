#!/usr/bin/python3
"""Contains a JSON-to-object function."""
import json


def from_json_string(my_str):
    """Returns an object loaded from a JSON string."""
    return json.loads(my_str)
