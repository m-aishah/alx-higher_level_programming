#!/usr/bin/python3
"""Appends to the end of a text file."""


def append_write(filename="", text=""):
    """Append a string to the end of a text file.

    Args:
        filename (str): The name of the file to append.
        text (str): The string to append at the end of the file.
    Returns:
        the number of characters added.
    """
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
