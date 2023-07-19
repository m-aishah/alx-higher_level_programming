#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_numbers = set(my_list)
    sum = 0

    for number in unique_numbers:
        sum += number
    return sum
