#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """A class representing a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize an instance of Student.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of Student.

        If attrs is a list of strings, only attribute names
        contained in this list must be retrieved.

        Args:
            attrs (list): The attributes to retrieve."""
        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attribute of a Student."""
        for k, v in json.item():
            setattr(self, k, v)
