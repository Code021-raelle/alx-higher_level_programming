#!/usr/bin/python3
"""
This module provides a test for a string printing module
"""


def say_my_name(first_name, last_name=""):
    """
    Function to print a string with provided names
    Args:
        first_name: first name string
        last_name: last name optional string
    """
    if type(first_name) != str:
        raise TypeError('first_name must be a string')
    if type(last_name) != str:
        raise TypeError('last_name must be a string')

    print("My name is {} {}".format(first_name, last_name))
