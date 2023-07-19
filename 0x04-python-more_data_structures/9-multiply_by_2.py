#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """A function that returns a new dictionary with all values multiplied by 2"""
    return ({key: a_dictionary[key] * 2 for key in a_dictionary})
