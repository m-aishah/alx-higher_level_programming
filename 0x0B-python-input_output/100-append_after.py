#!/usr/bin/python3
"""Formats a text file according to some criteria."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for.
        new_string (str): The string to be inserted.
    """
    text = ""
    with open(filename) as f_r:
        for line in f_r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as f_w:
        f_w.write(text)
