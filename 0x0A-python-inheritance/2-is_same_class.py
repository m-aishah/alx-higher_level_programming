#!/usr/bin/python3
"""Function to confirm the instance of a class."""


def is_same_class(obj, a_class):
    """Check if object is an instance of a class.

    Returns:
        True if obj is exactly an instance of a_class.
        Otherwise returns False.
    """
    if type(obj) == a_class:
        return True
    return False
