#!/usr/bin/python3
def number_keys(a_dictionary):
    """ Returns the number of keys in a dictionary."""
    # return (len(a_dictionary))
    num_keys = 0
    for k in a_dictionary.items():
        num_keys = num_keys + 1
    return num_keys
