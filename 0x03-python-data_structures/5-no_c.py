#!/usr/bin/python3
def no_c(my_string):
    new_list = [char for char in my_string if char not in ['c', 'C']]
    new_string = ''.join(new_list)
    return new_string
