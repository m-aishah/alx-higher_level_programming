#!/usr/bin/python3
"""Returns a dictionary representation of a Python object."""


def class_to_json(obj):
    """Return the dictionary description of a simple data structure."""
    return obj.__dict__
