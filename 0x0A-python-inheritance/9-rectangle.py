#!/usr/bin/python3
"""Defines a child class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A child class that represents a rectangle."""
    def __init__(self, width, height):
        """Initialize an instance of the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of te rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of a rectangle."""
        return(self.__width * self.__height)

    def __str__(self):
        """Returns rectangle description."""
        description = "[" + str(self.__class__.__name__) + "] "
        description += str(self.__width) + "/" + str(self.__height)
        return description
