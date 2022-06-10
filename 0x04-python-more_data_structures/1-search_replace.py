#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replaces all occurrences of an element by another in a new list."""
    new_list = my_list[:]
    for x in range(len(new_list)):
        if new_list[x] == search:
            new_list[x] = replace
    return new_list
