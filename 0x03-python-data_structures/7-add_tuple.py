#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    # If a tuple is smaller than 2,
    # use the value 0 for each missing integer
    # take care of tuple_a
    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            tuple_a = 0, 0
        else:
            tuple_a = tuple_a[0], 0
    # take care of tuple_b
    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            tuple_b = 0, 0
        else:
            tuple_b = tuple_b[0], 0

    return ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))
