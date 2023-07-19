#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """Returns a list of values multilied by a number"""
    return list(map(lambda x: x * number, my_list[:]))
