#!/usr/bin/python3
""" Defining a class called Rectangle. """


class Rectangle:
    """" Defining the class Rectangle. """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Getter method for private instance attributewidth. """

        return(self.__width)

    @width.setter
    def width(self, value):
        """ Setter method for private instance attribute height.

        Args:
            value (int): The width of an instance of Rectangle.
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('widt must be >= 0')
        self.__width = value

    @property
    def height(self):
        """ Getter method for private instance attribute height. """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter method for private instance attribute height.

        Args:e
            value (int): The height of an instance of Rectangle.
        """
        if type(value) is not int:
            raise TypeError('heigt must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
