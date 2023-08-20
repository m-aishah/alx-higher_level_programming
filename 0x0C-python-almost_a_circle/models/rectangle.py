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
        [print() for k in range (self.y)]
        for i in range (self.height):
            [print(' ', end='') for l in range (self.x)]
            [print('#', end='') for j in range (self.width)]
            print()

    def __str__(self):
        string = '[Rectangle] (' + str(self.id) + ') ' + str(self.x)
        string += '/' + str(self.y) + ' - ' + str(self.width)
        string += '/' + str(self.height)
        return string

    def update(self, *args, **kwargs):
        no_of_arguments = len(args)
        a = 0

        if args and no_of_arguments:
            if no_of_arguments > a:
                if args[0] is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                else:
                    self.id = args[0]
                a += 1
            if no_of_arguments > a:
                self.width = args[1]
                a += 1
            if no_of_arguments > a:
                self.height = args[2]
                a += 1
            if no_of_arguments > a:
                self.x = args[3]
                a += 1
            if no_of_arguments > a:
                self.y = args[4]
        elif kwargs:
            if 'id' in kwargs:
                if kwargs['id'] is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                else:
                    self.id = kwargs['id']
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

r1 = Rectangle(10, 10, 10, 10)
print(r1)

r1.update(height=1)
print(r1)

r1.update(width=1, x=2)
print(r1)

r1.update(y=1, width=2, x=3, id=89)
print(r1)

r1.update(x=1, height=2, y=3, width=4)
print(r1)
