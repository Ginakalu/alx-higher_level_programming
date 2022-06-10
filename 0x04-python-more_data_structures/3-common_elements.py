#!/usr/bin/python3
def common_elements(set_1, set_2):
    """ Returns a set of common elements in two sets."""
    # return (set_1 & set_2)
    common_set = set()
    for x in set_1:
        if x in set_2:
            common_set.add(x)
    return common_set
