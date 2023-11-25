#!/usr/bin/python3
'''Finds the peak in a list of integers.'''


def find_peak_recursive(list_of_integers, left_index, right_index):
    '''Return the peak number in the list of integers.'''
    if left_index == right_index:
        return list_of_integers[left_index]

    mid_index = (left_index + right_index) // 2

    if list_of_integers[mid_index] < list_of_integers[mid_index + 1]:
        return find_peak_recursive(list_of_integers,
                                   mid_index + 1, right_index)
    else:
        return find_peak_recursive(list_of_integers, left_index, mid_index)


def find_peak(list_of_integers):
    '''Return the peak number in the list of integers.'''
    length = len(list_of_integers)
    if length == 0:
        return None
    else:
        return find_peak_recursive(list_of_integers, 0, length - 1)
