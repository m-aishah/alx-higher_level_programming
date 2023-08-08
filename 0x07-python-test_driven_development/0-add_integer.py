#!/usr/bin/python3
"""Defines a function that adds 2 integers."""


def add_integer(a, b=98):
    """Returns the integer addition of `a` and `b`.

    `a` and `b` must be first casted to integers if they are float.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Raises:
        TypeError: If either `a` or `b` is not an integer or float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return(int(a) + int(b))
