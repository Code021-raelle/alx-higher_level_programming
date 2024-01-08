#!/usr/bin/python3
"""This module inherits from the class list"""


class MyList(list):
    """Class that inherits from list"""
    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
