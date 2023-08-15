#!/usr/bin/python3
"""Contains a create Object-from-JSON file function."""
import json


def load_from_json_file(filename):
    """Returns an object loaded from a JSON file."""
    with open(filename, 'r') as f:
        return json.load(f)
