#!/usr/bin/python3
"""MagicClass class gotten from interpreting bytecodes provided by ALX"""


import math


class MagicClass:
    """Defining the MagicClass class."""

    def __init__(self, radius=0):
        """initializes new instance of the MagicClass.

        Arg:
            radius (int): radius of the current instance of the class.
        """
        if not isinstance(radius, int) and not isinstance(radius, float):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """returns the area of the MagicClass."""
        return(self.__radius ** 2 * math.pi)

    def circumference(self):
        """Returns the circumference of the MagicClass."""
        return(2 * math.pi * self.__radius)
