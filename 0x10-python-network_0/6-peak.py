#!/usr/bin/python3
""" Implement the find_peak function """


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers using binary search.

    Parameters:
    list_of_integers (list): A list of unsorted integers.

    Returns:
    int: The value of the peak if found, otherwise None.
    """
    if not list_of_integers:
        return None

    low = 0
    high = len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid

    # Check if the found peak is indeed a peek
    if low == 0 or low == len(list_of_integers) - 1:
        return list_of_integers[low]
    if list_of_integers[low] > list_of_integers[low - 1] and list_of_integers[low] > list_of_integers[low + 1]:
        return list_of_integers[low]
    return None
