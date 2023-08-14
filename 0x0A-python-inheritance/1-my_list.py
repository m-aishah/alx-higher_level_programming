#!/usr/bin/python3
"""Defines a class that inherits from list class."""


class MyList(list):
    """Child class."""

    def print_sorted(self):
        """Print list in sorted ascending order."""
        print(sorted(self))
