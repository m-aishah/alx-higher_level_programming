#!/usr/bin/python3
""" Representing a class called Rectangle. """


class Rectangle:
    """ Defining a Rectangle. """
    def __init__(self, width=0, height=0):
        """ Initializes a new Rectangle.

        Args:
            width (int):    The width of the new instance of Rectangle
            height (int): The height of the new instance of Rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Gets/sets the width of a rectangle. """
        return(self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """ Gets/sets the height of a rectangle. """
        return(self.__width)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """ Returns the area of a rectangle. """
        return(self.__width * self.__height)

    def perimeter(self):
        """ Returns the perimeter of a rectangle. """
        if self.__height == 0 or self.__width == 0:
            return(0)
        return(2 * (self.__height + self.__width))
