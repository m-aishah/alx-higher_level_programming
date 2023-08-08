#!/usr/bin/python3
""" Defines a class called LockedClass. """


class LockedClass:
    """ LockedClass

    Prevents the user from dynamically creating new instance,
    except it is called 'first_name'.
    """

    __slots__ = ["first_name"]
