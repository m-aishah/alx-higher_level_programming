#!/usr/bin/python3
'''Define a class called Square.'''
import sys
sys.path.append('/root/alx-higher_level_programming/0x0C-python-almost_a_circle/models')
from rectangle import Rectangle


class Square(Rectangle):
    '''Represents a square.'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Create a new instance of Square.

        Args:
            size (int): width and height of the square.
            x (int): x coordinate of the square.
            y (int): y coordinate of the square.
        '''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''Getter/setter for size of the Square.'''
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        '''Return the print() and str() representation of a square.'''
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x, self.y,
                                                 self.width)

    def update(self, *args, **kwargs):
        '''Update a Square.

        Args:
            *args (ints): New attribute values.
                - 1st argument should be the id attribute
                - 2nd argument should be the size attribute
                - 3rd argument should be the x attribute
                - 4th argument should be the y attribute
            **kwargs (dict): Keyworded arguments.
        '''
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
                self.size = args[1]
                a += 1
            if no_of_arguments > a:
                self.x = args[2]
                a += 1
            if no_of_arguments > a:
                self.y = args[3]
        elif kwargs:
            if 'id' in kwargs:
                if kwargs['id'] is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                else:
                    self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        '''Return the dictionary representation of a Square.'''
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }

