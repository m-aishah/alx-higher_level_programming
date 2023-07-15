#!/usr/bin/python3
def max_integer(my_list=[]):
    max = 'None'
    if my_list:
        max = my_list[0]
        for integer in my_list:
            if integer > max:
                max = integer
    return max
