#!/usr/bin/python3
"""Define class Base."""
import json


class Base:
    """A Base class."""

    __nb_objects = 0

    def __init__(self, id=None):
        '''Initailize the Base class.'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Returns the JSON representation of a list of dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries to be converted.
        Returns:
            '[]': if list_dictionaries is empty or None.
            else, the JSON representation of list_dictionaries.'''
        if list_dictionaries is None or list_dictionaries == []:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Write the JSON representation of a list of objects to a file.

        Args:
            list_objs (list): A list of instances of child classes.
        '''
        filename = cls.__name__ + '.json'
        with open(filename, 'w', encoding='utf-8') as f:
            if list_objs is None:
                f.write('[]')
            else:
                list_dictionaries = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        '''Converts a JSON string representation to list of dictionaries.

        Args:
            json_string (str): A string representing a list of dictionaries.
        Returns:
            An empty list: if json_string is None or empty.
            else, returns the list represented by json_string.
        '''
        if json_string is None or json_string == '[]':
            return []
        else:
            json.loads(json_string)
