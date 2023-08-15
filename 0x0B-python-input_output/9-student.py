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

    def to_json(self):
        """Retrieve a dictionary representation of Student."""
        return self.__dict__
