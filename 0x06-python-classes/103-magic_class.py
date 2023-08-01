#!/usr/bin/python3
"""MagicClass class gotten from interpreting bytecodes provided by ALX"""

import math


class MagicClass:
    """MagicClass - Represent a circle."""

    def __init__(self, radius=0):
        """Initializes a new instance of the MagicClass.

        Arg:
            radius (float or int): The radius of the new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Returns the area of the MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Returns the circumference of the MagicClass."""
        return (2 * math.pi * self.__radius)
