#!/usr/bin/python3
"""Reads a text file."""


def read_file(filename=""):
    """Read a text file and print it to stdout."""
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
