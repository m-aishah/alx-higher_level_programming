#!/usr/bin/python3
"""Defines a base class."""


class BaseGeometry:
    """A class for geometry."""

    def area(self):
        """raises an exception."""
        raise Exception('area() is not implemented')
