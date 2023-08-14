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
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
