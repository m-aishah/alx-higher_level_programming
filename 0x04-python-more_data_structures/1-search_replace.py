#!/usr/bin/python3
def search_replace(my_list, search, replace):
    duplicate_list = my_list[:]
    for i in range(len(duplicate_list)):
        if duplicate_list[i] == search:
            duplicate_list[i] = replace
    return duplicate_list
