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
        if type(value) is not int and type(value) is not float:
            raise TypeError('size must be a number')

        elif value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    def area(self):
        """Returns the current area of a square."""
        return (self.__size ** 2)

    def __eq__(self, r_operand):
        """Defining te == operator for comparison between
            2 instances of the class.
        """
        return (self.area() == r_operand.area())

    def __ne__(self, r_operand):
        """Defining te != operator for comparison between
            2 instances of the class.
        """
        return (self.area() != r_operand.area())

    def __lt__(self, r_operand):
        """Defining te < operator for comparison between
            2 instances of the class.
        """
        return (self.area() < r_operand.area())

    def __gt__(self, r_operand):
        """Defining te > operator for comparison between
            2 instances of the class.
        """
        return (self.area() > r_operand.area())

    def __le__(self, r_operand):
        """Defining te <= operator for comparison betweene
            2 instances of the class.
        """
        return (self.area() <= r_operand.area())

    def __ge__(self, r_operand):
        """Defining the >= operator for comparison betweene
            2 instances of the class.
        """
        return (self.area() >= r_operand.area())
