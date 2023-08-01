#!/usr/bin/python3
"""Defining the class called Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Method to initialize a new instance of Square.

        Args:
            size (int): The size of the square.
            position (int, int): The position of the square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get the current position of the square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Set te position of the square"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Returns the current area of a square."""
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square with '#' to the stdout."""
        if self.__size == 0:
            print()
            return

        [print() for i in range(self.__position[1])]
        for i in range(0, self.__size):
            [print(' ', end="") for j in range(self.__position[0])]
            [print('#', end="") for k in range(self.__size)]
            print()

    def __str__(self):
        self.my_print()
        return ('')
