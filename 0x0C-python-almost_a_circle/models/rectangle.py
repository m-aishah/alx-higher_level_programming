#!/usr/bin/python3
'''Child class Rectangle.'''
import sys
sys.path.append('/root/alx-higher_level_programming/0x0C-python-almost_a_circle/models')
from base import Base


class Rectangle(Base):
    '''Represent a rectangle.'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Create an instance of rectangle.

        Args:
            width (int): The width fo the rectangle.
            height (int): The height of the rectangle.
            x (int): The x coordinate of the rectangle.
            y (int): The y coordinate of the rectangle.
            id (int): The id no. of the rectangle.
        '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''Getter for private instance attribute - width.'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Setter for private instance attribute - width.'''
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        '''Getter for private instance attribute - height.'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Setter for private instance attribute - height.'''
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        '''Getter for private instance attribute - x.'''
        return self.__x

    @x.setter
    def x(self, value):
        '''Setter for private instance attribute - x.'''
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        '''Getter for private instance attribute - y.'''
        return self.__y

    @y.setter
    def y(self, value):
        '''Setter for private instance attribute - y.'''
        if type(value) != int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        '''Return the area of the rectangle.'''
        return self.width * self.height

    def display(self):
        '''Print a rectangle with # characters.'''
        for i in range (self.height):
            [print('#', end='') for j in range (self.width)]
            print()

r1 = Rectangle(4, 6)
r1.display()
