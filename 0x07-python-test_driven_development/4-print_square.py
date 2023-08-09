#!/usr/bin/python3
"""Defining a function that prints a square."""


def print_square(size):
    """Print a square with the characer #.

    Args:
        size (int): The size length of the square.
    Raises:
        TypeError: if size is not an integer.
        ValueError: if size is < 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print()
