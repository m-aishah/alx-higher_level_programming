#!/usr/bin/python3
"""Defines a child class Square that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square in geometry."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of a Square."""
        return(self.__size ** 2)

    def __str__(self):
        """Returns Square description."""
        description = "[" + str(self.__class__.__name__) + "] "
        description += str(self.__size) + "/" + str(self.__size)
        return description
