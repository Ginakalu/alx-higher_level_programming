#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Adds all unique integers in a list (only once for each integer)."""
    # return (sum(set(my_list)))

    total = 0
    for x in set(my_list):
        total += x
    return total
