#!/usr/bin/python3
"""Defines a sub-class checking function."""


def inherits_from(obj, a_class):
    """Check if a class an inherited instance of another class.

    Returns:
        True if obj is an inherited instance of a_class.
        Otherwise, returns False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
