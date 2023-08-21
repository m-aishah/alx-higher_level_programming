#!/usr/bin/python3
"""Unittest for Base class."""
import sys
sys.path.append('/root/alx-higher_level_programming/0x0C-python-almost_a_circle/models')
import os
import unittest
from base import Base
from rectangle import Rectangle
from square import Square


class TestBaseClass(unittest.TestCase):
    """Unittests for Base class."""

    def setUp(self):
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base(None)
        self.b4 = Base(12)
        self.b5 = Base()

    def test_init(self):
        """Test the constructor."""
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 3)
        self.assertEqual(self.b4.id, 12)
        self.assertEqual(self.b5.id, 4)

class TestBase_to_json_string(unittest.TestCase):
    '''Unittests for the to_json_string method.'''

    def test_to_json_string_rectangle_type(self):
        '''Check that the method returns str if called with list of Rectangle dict.'''
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_string_rectangle_one_dict(self):
        '''Test the method with a list of one Rectangle dictionary.'''
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 53)

    def test_to_json_string_rectangle_two_dicts(self):
        '''Test the method wih a list of two dictionaries of rectangles.'''
        r1 = Rectangle(2, 3, 5, 19, 2)
        r2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)

    def test_to_json_string_square_type(self):
        '''Check that the method returns a string when called with Square dictionary.'''
        s = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_to_json_string_square_one_dict(self):
        '''Test the method with a list of one Square dictionary.'''
        s = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([s.to_dictionary()])) == 39)

    def test_to_json_string_square_two_dicts(self):
        '''Test the method with a list of two Square dictionaries.'''
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)

    def test_to_json_string_empty_list(self):
        '''Test the method with an empty list.'''
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        '''Test the method with None.'''
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args(self):
        '''Test the method with no argunets.'''
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        '''Test the method with more than one arguments.'''
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


class TestBase_save_to_file(unittest.TestCase):
    '''Unittests for the class method - save_to_file.'''

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_one_rectangle(self):
        '''Test the method with a list of two rectangles.'''
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    def test_save_to_file_two_rectangles(self):
        '''Test the method with a list of two rectangles.'''
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 105)

    def test_save_to_file_one_square(self):
        '''Test the method with a list of one square.'''
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_two_squares(self):
        '''Test the method with a list of two squares.'''
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 77)

    def test_save_to_file_cls_name_for_filename(self):
        '''Ensure the filename is correct - <class_name>.json'''
        s = Square(10, 7, 2, 8)
        Base.save_to_file([s])
        with open("Base.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_overwrite(self):
        ''' Check that the method overites the file.'''
        s = Square(9, 2, 39, 2)
        Square.save_to_file([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_None(self):
        '''Test the method with None.'''
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty_list(self):
        '''Test the method with an empty list.'''
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_no_args(self):
        '''Test the method with no arguments.'''
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_more_than_one_arg(self):
        '''Test the method with more tan one arguments.'''
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)

class TestBase_from_json_string(unittest.TestCase):
    '''Unittests for static method - from_json_string.'''

    def test_from_json_string_return_type(self):
        '''Check that the method returns a list.'''
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def test_from_json_string_one_rectangle(self):
        '''Test the  method with a list of one rectangle.'''
        list_input = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_rectangles(self):
        '''Test the method with a list of two rectangles.'''
        list_input = [
            {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
            {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_one_square(self):
        '''Test the method with a list of one Square.'''
        list_input = [{"id": 89, "size": 10, "height": 4}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_squares(self):
        '''Test the method with a list of two Squares.'''
        list_input = [
            {"id": 89, "size": 10, "height": 4},
            {"id": 7, "size": 1, "height": 7}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_None(self):
        '''Test the method with None.'''
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        '''Test the method with an empty list.'''
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_no_args(self):
        '''Test the method with no arguments.'''
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_more_than_one_arg(self):
        '''Test the method with more than one arguments.'''
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)

if __name__ == '__main__':
    unittest.main()
