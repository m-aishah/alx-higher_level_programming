#!/usr/bin/python3
"""Contains a write object to file function."""
import json


def save_to_json_file(my_obj, filename):
    """Write object to a text file using JSON representation.

    Args:
        my_obj (str): The object to write.
        file_name (str): The name of the file to write into.
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)
