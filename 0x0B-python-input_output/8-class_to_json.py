#!/usr/bin/python3
"""Contains a class-to-JSON file."""


def class_to_json(obj):
    """Return the dictionary description of a simple data structure."""
    return obj.__dict__
