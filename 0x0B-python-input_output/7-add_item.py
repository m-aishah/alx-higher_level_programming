#!/usr/bin/python3
"""Loads, adds and saves arguments into a file."""
import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        args_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        args_list = []
    args_list.extend(sys.argv[1:])
    save_to_json_file(args_list, "add_item.json")
