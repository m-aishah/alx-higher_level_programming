#!/usr/bin/python3
"""Defines a base class."""


class BaseGeometry:
    """A base class for geometry."""

    def area(self):
        """Raises an Exception."""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates a parameter as an integer.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is <= 0.
        """
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
