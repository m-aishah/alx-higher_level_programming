#!/usr/bin/python3
"""Defining the class called Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Method to initialize a new instance of Square.

        Args:
            size (int): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Get the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')

        elif value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    def area(self):
        """Returns the current area of a square."""
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square with '#' to the stdout."""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end="")
            print()
