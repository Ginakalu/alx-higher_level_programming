#!/usr/bin/python3

"""Defines an inherited list MyList"""


class MyList(list):
    """Implements sorted printing for inherited class"""

    def print_sorted(self):
        """Prints list in ascending order"""
        print(sorted(self))
