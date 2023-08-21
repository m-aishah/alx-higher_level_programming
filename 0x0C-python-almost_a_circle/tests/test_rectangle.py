#!/usr/bin/python3
'''Unittest for class Rectangle.'''
import unittest
import sys
sys.path.append('/root/alx-higher_level_programming/0x0C-python-almost_a_circle/models')
import io
from rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    '''Unittests for Rectangle class.'''

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

    def test_string_id(self):
        '''Create an instance of Rectangle with an id that not an integer.'''
        r13 = Rectangle(16, 18, 0, 4, 'a_string')
        self.assertEqual(r13.width, 16)
        self.assertEqual(r13.height, 18)
        self.assertEqual(r13.x, 0)
        self.assertEqual(r13.y, 4)
        self.assertEqual(r13.id, 'a_string')

    def test_invalid_width(self):
        '''Check that fails when the width is not integer.'''
        with self.assertRaises(TypeError):
            r7 = Rectangle('not_an_integer', 4, 1, 1)

    def test_invalid_height(self):
        '''Check that fails when the height is not integer.'''
        with self.assertRaises(TypeError):
            r8 = Rectangle(2, 'not_an_integer', 1, 1)

    def test_invalid_x(self):
        '''Check that fails when the x coordinate is not an integer.'''
        with self.assertRaises(TypeError):
            r7 = Rectangle(2, 4, 'not_an_integer', 1)

    def test_invalid_y(self):
        '''Check that fails when the y coordinate is not an integer.'''
        with self.assertRaises(TypeError):
            r8 = Rectangle(2, 4, 1, 'not_an_integer')

    def test_negative_width(self):
        '''Check that fails when the width is negative.'''
        with self.assertRaises(ValueError):
            r9 = Rectangle(-2, 4, 1, 1)

    def test_negative_height(self):
        '''Check that fails when the height is negative.'''
        with self.assertRaises(ValueError):
            r10 = Rectangle(2, -5, 1, 2)

    def test_zero_width(self):
        '''Check that fails when the width is 0.'''
        with self.assertRaises(ValueError):
            r9 = Rectangle(0, 4, 1, 1)

    def test_zero_height(self):
        '''Check that fails when the height is 0.'''
        with self.assertRaises(ValueError):
            r10 = Rectangle(2, 0, 1, 2)

    def test_negative_x(self):
        '''Check that fails when the x coordinate is negative.'''
        with self.assertRaises(ValueError):
            r9 = Rectangle(2, 4, -1, 1)

    def test_negative_y(self):
        '''Check that fails when the y coordinate is negative.'''
        with self.assertRaises(ValueError):
            r10 = Rectangle(2, 5, 1, -2)

    def test_negative_arguments(self):
        '''Check that fails when the width and height is negative.'''
        with self.assertRaises(ValueError):
            r11 = Rectangle(-2, -5, -3, -11, -1)

    def test_invalid_argument(self):
        with self.assertRaises(TypeError):
            r12 = Rectangle(None)

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


if __name__ == '__main__':
    unittest.main()