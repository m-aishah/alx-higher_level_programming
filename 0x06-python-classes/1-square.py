#!/usr/bin/python3
"""Defining the class called Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Method to initialize a new instance of Square.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
