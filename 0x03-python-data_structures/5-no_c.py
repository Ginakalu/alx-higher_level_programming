#!/usr/bin/python3
def no_c(my_string):
    # new_str = ""
    # for i in my_string:
    #     if i != 'c' and i != 'C':
    #         new_str += i
    # return new_str
    new_str = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(new_str))
