#!/usr/bin/python3
"""Contain a function that writes into a text file."""


def write_file(filename="", text=""):
    """Write into a string into a text file.

    Args:
        filename (str): The name of the file to write into.
        text (str): The string to write into the file.
    Returns:
        The number of characters written.
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
