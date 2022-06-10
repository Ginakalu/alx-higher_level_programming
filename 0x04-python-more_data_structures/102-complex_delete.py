#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """Delete keys with a specific value in a dictionary."""
    for x in list(a_dictionary):
        if a_dictionary[x] == value:
            del a_dictionary[x]

    return a_dictionary
