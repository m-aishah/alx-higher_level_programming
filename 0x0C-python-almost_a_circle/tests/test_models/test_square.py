#!/usr/bin/python3
'''Unittests for Square class.'''
import unittest
import io
import sys
sys.path.append('/root/alx-higher_level_programming/0x0C-python-almost_a_circle/models')
from square import Square
from rectangle import Rectangle
from base import Base


class TestSquare_init(unittest.TestCase):
    '''Testing the init method.'''

    def test_is_base(self):
        '''Test that Square is an instance of he Base class.'''
        self.assertIsInstance(Square(5), Base)

    def test_is_rectangle(self):
        '''Test tha the Square is an instance of the Rectangle class.'''
        self.assertIsInstance(Square(5), Rectangle)

    def test_no_arguments(self):
        '''Create an instance of square with no attributes.'''
        with self.assertRaises(TypeError):
            Square()

    def test_one_argument(self):
        '''Create an instance of square with one argument.'''
        s1 = Square(4)
        s2 = Square(20)
        self.assertEqual(s1.width, 4)
        self.assertEqual(s1.height, 4)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, s2.id - 1)

    def test_two_argument(self):
        '''Create an instance of square with two argument.'''
        s1 = Square(4, 7)
        s2 = Square(20, 3)
        self.assertEqual(s1.width, 4)
        self.assertEqual(s1.height, 4)
        self.assertEqual(s1.x, 7)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, s2.id - 1)

    def test_three_argument(self):
        '''Create an instance of square with three argument.'''
        s1 = Square(4, 14, 6)
        s2 = Square(20, 3, 2)
        self.assertEqual(s1.width, 4)
        self.assertEqual(s1.height, 4)
        self.assertEqual(s1.x, 14)
        self.assertEqual(s1.y, 6)
        self.assertEqual(s1.id, s2.id - 1)

    def test_four_argument(self):
        '''Create an instance of square with four argument.'''
        s1 = Square(4, 14, 6, 5)
        self.assertEqual(s1.width, 4)
        self.assertEqual(s1.height, 4)
        self.assertEqual(s1.x, 14)
        self.assertEqual(s1.y, 6)
        self.assertEqual(s1.id, 5)

    def test_more_than_four_arguments(self):
        '''Create an instance with more than four arguments.'''
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5, 6)


class TestSquare_size_attribute(unittest.TestCase):
    '''unittests on the private instance attribute - size.'''

    def test_private_size(self):
        '''Check that the size is a private attribute.'''
        with self.assertRaises(AttributeError):
            print(Square(5).__size)

    def test_size_getter(self):
        '''Test the size getter method.'''
        s = Square(2)
        self.assertEqual(s.size, 2)

    def test_size_setter(self):
        '''Test the size setter method.'''
        s = Square(2)
        s.size = 12
        self.assertEqual(s.size, 12)

    def test_None_size(self):
        '''Check that error is raised when size equals None.'''
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Square(None)

    def test_string_size(self):
        '''Check that error is raised when the size is a string.'''
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Square('a_string')

    def test_float_size(self):
        '''Check that error is raised when the size is a float.'''
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Square(10.2)

    def test_dict_size(self):
        '''Check that error is raised when the siz is a dictionary.'''
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Square({'key': 2})

    def test_list_size(self):
        '''Check that error is raised when the size is a list.'''
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Square([1, 2, 3])

    def test_tuple_size(self):
        '''Check that error is raised when the size is a tuple.'''
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Square((10, 2))

    def test_nan_size(self):
        '''Check that error is raised when the size is a nan.'''
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Square(float('nan'))

    def test_zero_size(self):
        '''Check that fails when the size is 0.'''
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            r9 = Square(0)

    def test_negative_size(self):
        '''Check that fails when the size is negative.'''
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            r9 = Square(-2)


class TestSquare_x_attribute(unittest.TestCase):
    '''Unittests for the x attribute.'''

    def test_private_x(self):
        '''Check that the x is a private attribute.'''
        with self.assertRaises(AttributeError):
            print(Square(5, 4, 5, 5).__x)

    def test_x_getter(self):
        '''Test the x getter method.'''
        r7 = Square(2, 5, 1, 1)
        self.assertEqual(r7.x, 5)

    def test_x_setter(self):
        '''Test the x setter method.'''
        r7 = Square(2, 4)
        r7.x = 12
        self.assertEqual(r7.x, 12)

    def test_None_x(self):
        '''Check that error is raised when x equals None.'''
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Square(5, None)

    def test_string_x(self):
        '''Check that error is raised when the x is a string.'''
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Square(4, 'a_string', 1)

    def test_float_x(self):
        '''Check that error is raised when the x is a float.'''
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Square(4, 10.2, 1)

    def test_dict_x(self):
        '''Check that error is raised when the x is a dictionary.'''
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Square(4, {'key': 2}, 1)

    def test_list_x(self):
        '''Check that error is raised when the x is a list.'''
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Square(4, [1, 2, 3], 1)

    def test_tuple_x(self):
        '''Check that error is raised when the x is a tuple.'''
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Square(4, (10, 2), 1)

    def test_nan_x(self):
        '''Check that error is raised when the x is a nan.'''
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Square(4, float('nan'), 1)

    def test_negative_x(self):
        '''Check that fails when the x coordinate is negative.'''
        with self.assertRaises(ValueError):
            r9 = Square(2, -1, 1)


class TestSquare_y_attribute(unittest.TestCase):
    '''Unittests for the y attribute.'''

    def test_private_y(self):
        '''Check that the y is a private attribute.'''
        with self.assertRaises(AttributeError):
            print(Square(5, 4, 5, 5).__y)

    def test_y_getter(self):
        '''Test the y getter method.'''
        r7 = Square(2, 1, 5, 1)
        self.assertEqual(r7.y, 5)

    def test_y_setter(self):
        '''Test the y setter method.'''
        r7 = Square(2, 4, 4)
        r7.y = 12
        self.assertEqual(r7.y, 12)

    def test_None_y(self):
        '''Check that error is raised when y equals None.'''
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Square(5, 4, None)

    def test_string_y(self):
        '''Check that error is raised when the y is a string.'''
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Square(4, 4, 'a_string', 1)

    def test_float_y(self):
        '''Check that error is raised when the y is a float.'''
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Square(4, 4, 10.2, 1)

    def test_dict_y(self):
        '''Check that error is raised when the y is a dictionary.'''
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Square(4, 4, {'key': 2}, 1)

    def test_list_y(self):
        '''Check that error is raised when the y is a list.'''
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Square(4, 4, [1, 2, 3], 1)

    def test_tuple_y(self):
        '''Check that error is raised when the y is a tuple.'''
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Square(4, 4, (10, 2), 1)

    def test_nan_y(self):
        '''Check that error is raised when the y is a nan.'''
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Square(4, 4, float('nan'), 1)

    def test_negative_y(self):
        '''Check that fails when the y coordinate is negative.'''
        with self.assertRaises(ValueError):
            r9 = Square(2, 4, -1, 1)


class TestSquare_area(unittest.TestCase):
    '''Unittests for the area() method.'''

    def test_area(self):
        s = Square(4)
        self.assertEqual(s.area(), 16)


class TestSquare_output(unittest.TestCase):
    '''Test the display and __str__ methods.'''

    @staticmethod
    def capture_stdout(sq, method):
        '''Returns the output printed to the screen
        after using display or __str__.

        Args:
            sq (Square): The Square to be printed.
            method (str): The method to run on the rectangle.
        Returns:
        The text printed to the stdout.
        '''
        capture = io.StringIO()
        sys.stdout = capture

        if method == 'print':
            print(sq)
        else:
            sq.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_print(self):
        '''Test the __str__method.'''
        s = Square(4)
        capture = TestSquare_output.capture_stdout(s, 'print')
        expected = '[Square] ({}) 0/0 - 4\n'.format(s.id)
        self.assertEqual(capture.getvalue(), expected)

    def test_display_size(self):
        s = Square(2)
        capture = TestSquare_output.capture_stdout(s, "display")
        self.assertEqual("##\n##\n", capture.getvalue())


class TestSquare_update_args(unittest.TestCase):
    '''Unittests for the update args method of the Square class.'''

    def test_update_no_args(self):
        '''Test the update method with zero args.'''
        s = Square(10, 10, 10, 10)
        s.update()
        self.assertEqual(str(s), '[Square] (10) 10/10 - 10')

    def test_update_one_args(self):
        '''Test the update method with one args.'''
        s = Square(10, 10, 10, 10)
        s.update(89)
        self.assertEqual(str(s), '[Square] (89) 10/10 - 10')

    def test_update_two_args(self):
        '''Test the update method with two args.'''
        s = Square(10, 10, 10, 10)
        s.update(89, 2)
        self.assertEqual(str(s), '[Square] (89) 10/10 - 2')

    def test_update_three_args(self):
        '''Test the update method with three args.'''
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3)
        self.assertEqual(str(s), '[Square] (89) 3/10 - 2')

    def test_update_four_args(self):
        '''Test the update method with four args.'''
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3, 4)
        self.assertEqual(str(s), '[Square] (89) 3/4 - 2')

    def test_update_more_than_four_args(self):
        '''Test the update method with more than four args.'''
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3, 4, 5)
        self.assertEqual(str(s), '[Square] (89) 3/4 - 2')


class TestSquare_update_kwargs(unittest.TestCase):
    '''Unittests for the update kwargs method of the Square class.'''

    def test_update_no_kwargs(self):
        '''Test the update method with zero kwargs.'''
        s = Square(10, 10, 10, 10)
        s.update()
        self.assertEqual(str(s), '[Square] (10) 10/10 - 10')

    def test_update_one_kwargs(self):
        '''Test the update method with one kwargs.'''
        s = Square(10, 10, 10, 10)
        s.update(id=89)
        self.assertEqual(str(s), '[Square] (89) 10/10 - 10')

    def test_update_two_kwargs(self):
        '''Test the update method with two kwargs.'''
        s = Square(10, 10, 10, 10)
        s.update(id=89, size=2)
        self.assertEqual(str(s), '[Square] (89) 10/10 - 2')

    def test_update_three_kwargs(self):
        '''Test the update method with three kwargs.'''
        s = Square(10, 10, 10, 10)
        s.update(x=89, y=2, id=3)
        self.assertEqual(str(s), '[Square] (3) 89/2 - 10')

    def test_update_four_kwargs(self):
        '''Test the update method with four kwargs.'''
        s = Square(10, 10, 10, 10)
        s.update(size=89, id=2, y=3, x=4)
        self.assertEqual(str(s), '[Square] (2) 4/3 - 89')


class TestSquare_to_dictionary(unittest.TestCase):
    '''Unittests for the to_dictionary method.'''

    def test_to_dictionary_output(self):
        s = Square(10, 2, 1, 1)
        correct = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(correct, s.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        s1 = Square(10, 2, 1, 2)
        s2 = Square(1, 2, 10)
        s2.update(**s1.to_dictionary())
        self.assertNotEqual(s1, s2)

    def test_to_dictionary_arg(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            s.to_dictionary(1)


if __name__ == '__main__':
    unittest.main()
