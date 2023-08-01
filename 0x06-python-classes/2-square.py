#!/usr/bin/python3
"""Defining the class called Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Method to initialize a new instance of Square.

        Args:
            size (int): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
