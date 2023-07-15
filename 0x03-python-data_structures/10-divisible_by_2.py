#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        multiple_of_2 = []
        for integer in my_list:
            multiple_of_2.append(integer % 2 == 0)
        return multiple_of_2
