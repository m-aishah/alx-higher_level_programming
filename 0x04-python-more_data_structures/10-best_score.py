#!/usr/bin/python3
def best_score(a_dictionary):
    """A function that returns a key with the biggest integer value"""
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return 'None'
    max_key = list(a_dictionary.keys())[0]
    max_value = a_dictionary[max_key]

    for key in a_dictionary:
        if a_dictionary[key] > max_value:
            max_value = a_dictionary[key]
            max_key = key
    return max_key
