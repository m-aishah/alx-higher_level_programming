#!/usr/bin/python3
'''Unittest for class Rectangle.'''
import unittest
import sys
sys.path.append('/root/alx-higher_level_programming/0x0C-python-almost_a_circle/models')
import io
from rectangle import Rectangle
from base import Base


class TestRectangleClass_init(unittest.TestCase):
    '''Unittests for initialization of Rectangle class.'''

    def test_rectangle_is_base(self):
        '''Test that Rectangle inherits the Base class.'''
        self.assertIsInstance(Rectangle(5, 3), Base)

    def test_no_arguments(self):
        '''check that init fails when no argument is provided.'''
        with self.assertRaises(TypeError):
            r1 = Rectangle()

    def test_one_argument(self):
        '''Check that init fails when only 1 argument is passed.'''
        with self.assertRaises(TypeError):
            r2 = Rectangle(1)

    def test_two_arguments(self):
        '''Test init with two arguments provided.'''
        r3 = Rectangle(2, 4)
        self.assertEqual(r3.width, 2)
        self.assertEqual(r3.height, 4)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)
        self.assertTrue(r3.id is not None)

    def test_three_arguments(self):
        '''Try creating an instance of Rectangle with three arguments.'''
        r4 = Rectangle(4, 6, 1)
        self.assertEqual(r4.width, 4)
        self.assertEqual(r4.height, 6)
        self.assertEqual(r4.x, 1)
        self.assertEqual(r4.y, 0)
        self.assertTrue(r4.id is not None)

    def test_four_arguments(self):
        '''Try creating an instance of Rectangle with four arguments.'''
        r5 = Rectangle(8, 10, 1, 2)
        self.assertEqual(r5.width, 8)
        self.assertEqual(r5.height, 10)
        self.assertEqual(r5.x, 1)
        self.assertEqual(r5.y, 2)
        self.assertTrue(r5.id is not None)

    def test_five_arguments(self):
        '''Create inatance of Rectangle with all five arguments provided.'''
        r6 = Rectangle(12, 14, 6, 3, 24)
        self.assertEqual(r6.width, 12)
        self.assertEqual(r6.height, 14)
        self.assertEqual(r6.x, 6)
        self.assertEqual(r6.y, 3)
        self.assertEqual(r6.id, 24)

    def test_more_than_five_arguments(self):
        '''Create an instance with more than five arguments.'''
        with self.assertRaises(TypeError):
            Rectangle(22, 21, 4, 5, 6, 7)

    def test_string_id(self):
        '''Create an instance of Rectangle with an id that not an integer.'''
        r13 = Rectangle(16, 18, 0, 4, 'a_string')
        self.assertEqual(r13.width, 16)
        self.assertEqual(r13.height, 18)
        self.assertEqual(r13.x, 0)
        self.assertEqual(r13.y, 4)
        self.assertEqual(r13.id, 'a_string')


class TestRectangle_width_attribute(unittest.TestCase):
    '''Unittests for the width attribute.'''

    def test_private_width(self):
        '''Check that the width is a private attribute.'''
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 4, 5, 5).__width)

    def test_width_getter(self):
        '''Test the width getter method.'''
        r7 = Rectangle(2, 4, 5, 1, 1)
        self.assertEqual(r7.width, 2)

    def test_width_setter(self):
        '''Test the width setter method.'''
        r7 = Rectangle(2, 4, 5, 1, 1)
        r7.width = 12
        self.assertEqual(r7.width, 12)

    def test_None_width(self):
        '''Check that error is raised when width equals None.'''
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Rectangle(None, 5)

    def test_string_width(self):
        '''Check that error is raised when the width is a string.'''
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Rectangle('a_string', 4, 1, 1)

    def test_float_width(self):
        '''Check that error is raised when the width is a float.'''
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Rectangle(10.2, 4, 1, 1)

    def test_dict_width(self):
        '''Check that error is raised when the width is a dictionary.'''
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Rectangle({'key': 2}, 4, 1, 1)

    def test_list_width(self):
        '''Check that error is raised when the width is a list.'''
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Rectangle([1, 2, 3], 4, 1, 1)

    def test_tuple_width(self):
        '''Check that error is raised when the width is a tuple.'''
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Rectangle((10, 2), 4, 1, 1)

    def test_nan_width(self):
        '''Check that error is raised when the width is a nan.'''
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Rectangle(float('nan'), 4, 1, 1)

    def test_zero_width(self):
        '''Check that fails when the width is 0.'''
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            r9 = Rectangle(0, 4, 1, 1)

    def test_negative_width(self):
        '''Check that fails when the width is negative.'''
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            r9 = Rectangle(-2, 4, 1, 1)


class TestRectangle_height_attribute(unittest.TestCase):
    '''Unittests for the height attribute.'''

    def test_private_height(self):
        '''Check that the height is a private attribute.'''
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 4, 5, 5).__height)

    def test_height_getter(self):
        '''Test the height getter method.'''
        r7 = Rectangle(2, 4, 5, 1, 1)
        self.assertEqual(r7.height, 4)

    def test_height_setter(self):
        '''Test the height setter method.'''
        r7 = Rectangle(2, 4, 5, 1, 1)
        r7.height = 12
        self.assertEqual(r7.height, 12)

    def test_None_height(self):
        '''Check that error is raised when height equals None.'''
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(5, None)

    def test_string_height(self):
        '''Check that error is raised when the height is a string.'''
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(4, 'a_string', 1, 1)

    def test_float_height(self):
        '''Check that error is raised when the height is a float.'''
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(4, 10.2, 1, 1)

    def test_dict_height(self):
        '''Check that error is raised when the height is a dictionary.'''
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(4, {'key': 2}, 1, 1)

    def test_list_height(self):
        '''Check that error is raised when the height is a list.'''
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(4, [1, 2, 3], 1, 1)

    def test_tuple_height(self):
        '''Check that error is raised when the height is a tuple.'''
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(4, (10, 2), 1, 1)

    def test_nan_height(self):
        '''Check that error is raised when the height is a nan.'''
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(4, float('nan'), 1, 1)

    def test_zero_height(self):
        '''Check that fails when the height is 0.'''
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            r9 = Rectangle(4, 0, 1, 1)

    def test_negative_height(self):
        '''Check that fails when the height is negative.'''
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            r9 = Rectangle(2, -5, 1, 1)


class TestRectangle_x_attribute(unittest.TestCase):
    '''Unittests for the x attribute.'''

    def test_private_x(self):
        '''Check that the x is a private attribute.'''
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 4, 5, 5).__x)

    def test_x_getter(self):
        '''Test the x getter method.'''
        r7 = Rectangle(2, 4, 5, 1, 1)
        self.assertEqual(r7.x, 5)

    def test_x_setter(self):
        '''Test the x setter method.'''
        r7 = Rectangle(2, 4, 5, 1, 1)
        r7.x = 12
        self.assertEqual(r7.x, 12)

    def test_None_x(self):
        '''Check that error is raised when x equals None.'''
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Rectangle(5, 9, None)

    def test_string_x(self):
        '''Check that error is raised when the x is a string.'''
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Rectangle(4, 1, 'a_string', 1)

    def test_float_x(self):
        '''Check that error is raised when the x is a float.'''
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Rectangle(4, 1, 10.2, 1)

    def test_dict_x(self):
        '''Check that error is raised when the x is a dictionary.'''
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Rectangle(4, 1, {'key': 2}, 1)

    def test_list_x(self):
        '''Check that error is raised when the x is a list.'''
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Rectangle(4, 1, [1, 2, 3], 1)

    def test_tuple_x(self):
        '''Check that error is raised when the x is a tuple.'''
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Rectangle(4, 1, (10, 2), 1)

    def test_nan_x(self):
        '''Check that error is raised when the x is a nan.'''
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Rectangle(4, 1, float('nan'), 1)

    def test_negative_x(self):
        '''Check that fails when the x coordinate is negative.'''
        with self.assertRaises(ValueError):
            r9 = Rectangle(2, 4, -1, 1)


class TestRectangle_y_attribute(unittest.TestCase):
    '''Unittests for the y attribute.'''

    def test_private_y(self):
        '''Check that the y is a private attribute.'''
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 4, 5, 5).__y)

    def test_y_getter(self):
        '''Test the y getter method.'''
        r7 = Rectangle(2, 4, 5, 1, 1)
        self.assertEqual(r7.y, 1)

    def test_y_setter(self):
        '''Test the y setter method.'''
        r7 = Rectangle(2, 4, 5, 1, 1)
        r7.y = 12
        self.assertEqual(r7.y, 12)

    def test_None_y(self):
        '''Check that error is raised when y equals None.'''
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Rectangle(5, 9, 1, None)

    def test_string_y(self):
        '''Check that error is raised when the y is a string.'''
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Rectangle(4, 1, 1, 'a_string')

    def test_float_y(self):
        '''Check that error is raised when the y is a float.'''
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Rectangle(4, 1, 1, 10.2)

    def test_dict_y(self):
        '''Check that error is raised when the y is a dictionary.'''
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Rectangle(4, 1, 1, {'key': 2})

    def test_list_y(self):
        '''Check that error is raised when the y is a list.'''
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Rectangle(4, 1, 1, [1, 2, 3])

    def test_tuple_y(self):
        '''Check that error is raised when the y is a tuple.'''
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Rectangle(4, 1, 1, (10, 2))

    def test_nan_y(self):
        '''Check that error is raised when the y is a nan.'''
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Rectangle(4, 1, 1, float('nan'))

    def test_negative_y(self):
        '''Check that fails when the y coordinate is negative.'''
        with self.assertRaises(ValueError):
            r10 = Rectangle(2, 5, 1, -2)

    def test_negative_arguments(self):
        '''Check that fails when the width and y is negative.'''
        with self.assertRaises(ValueError):
            r11 = Rectangle(-2, -5, -3, -11, -1)

    def test_invalid_argument(self):
        with self.assertRaises(TypeError):
            r12 = Rectangle(None)


class TestRectangle_area(unittest.TestCase):
    '''Test area() method.'''

    def test_area(self):
        '''Test the area method.'''
        r14 = Rectangle(2, 3, 1, 1)
        self.assertEqual(r14.area(), 6)


class TestRectangle_output(unittest.TestCase):
    '''Test the display and __str__ methods.'''

    @staticmethod
    def capture_stdout(rect, method):
        '''Returns the output printed to the screen
        after using display or __str__.

        Args:
            rect (Rectangle): The rectangle to be printed.
            method (str): The method to run on the rectangle.
        Returns:
        The text printed to the stdout.
        '''
        capture = io.StringIO()
        sys.stdout = capture

        if method == 'print':
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_print(self):
        '''Test the __str__method.'''
        r15 = Rectangle(4, 6, 2, 1, 12)
        capture = TestRectangle_output.capture_stdout(r15, 'print')
        expected = '[Rectangle] (12) 2/1 - 4/6\n'
        self.assertEqual(capture.getvalue(), expected)

    def test_display_size(self):
        r = Rectangle(2, 2)
        capture = TestRectangle_output.capture_stdout(r, "display")
        self.assertEqual("##\n##\n", capture.getvalue())


class TestRectangle_update_args(unittest.TestCase):
    '''Unittests for the update args method of the Rectangle class.'''

    def test_update_no_args(self):
        '''Test the update method with zero args.'''
        r = Rectangle(10, 10, 10, 10, 10)
        r.update()
        self.assertEqual(str(r), '[Rectangle] (10) 10/10 - 10/10')

    def test_update_one_args(self):
        '''Test the update method with one args.'''
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89)
        self.assertEqual(str(r), '[Rectangle] (89) 10/10 - 10/10')

    def test_update_two_args(self):
        '''Test the update method with two args.'''
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2)
        self.assertEqual(str(r), '[Rectangle] (89) 10/10 - 2/10')

    def test_update_three_args(self):
        '''Test the update method with three args.'''
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3)
        self.assertEqual(str(r), '[Rectangle] (89) 10/10 - 2/3')

    def test_update_four_args(self):
        '''Test the update method with four args.'''
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4)
        self.assertEqual(str(r), '[Rectangle] (89) 4/10 - 2/3')

    def test_update_five_args(self):
        '''Test the update method with five args.'''
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), '[Rectangle] (89) 4/5 - 2/3')

    def test_update_more_than_five_args(self):
        '''Test the update method with more than five args.'''
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5, 6)
        self.assertEqual(str(r), '[Rectangle] (89) 4/5 - 2/3')


class TestRectangle_update_kwargs(unittest.TestCase):
    '''Unittests for the update kwargs method of the Rectangle class.'''

    def test_update_no_kwargs(self):
        '''Test the update method with zero kwargs.'''
        r = Rectangle(10, 10, 10, 10, 10)
        r.update()
        self.assertEqual(str(r), '[Rectangle] (10) 10/10 - 10/10')

    def test_update_one_kwargs(self):
        '''Test the update method with one kwargs.'''
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89)
        self.assertEqual(str(r), '[Rectangle] (89) 10/10 - 10/10')

    def test_update_two_kwargs(self):
        '''Test the update method with two kwargs.'''
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, width=2)
        self.assertEqual(str(r), '[Rectangle] (89) 10/10 - 2/10')

    def test_update_three_kwargs(self):
        '''Test the update method with three kwargs.'''
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(x=89, y=2, id=3)
        self.assertEqual(str(r), '[Rectangle] (3) 89/2 - 10/10')

    def test_update_four_kwargs(self):
        '''Test the update method with four kwargs.'''
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=89, id=2, height=3, x=4)
        self.assertEqual(str(r), '[Rectangle] (2) 4/10 - 89/3')

    def test_update_five_kwargs(self):
        '''Test the update method with five kwargs.'''
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, x=2, y=3, width=4, height=5)
        self.assertEqual(str(r), '[Rectangle] (89) 2/3 - 4/5')


class TestRectangle_to_dictionary(unittest.TestCase):
    '''Unittests for the to_dictionary method.'''

    def test_to_dictionary_output(self):
        r = Rectangle(10, 2, 1, 9, 5)
        correct = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertDictEqual(correct, r.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        r1 = Rectangle(10, 2, 1, 9, 5)
        r2 = Rectangle(5, 9, 1, 2, 10)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)

    def test_to_dictionary_arg(self):
        r = Rectangle(10, 2, 4, 1, 2)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)


if __name__ == '__main__':
    unittest.main()
