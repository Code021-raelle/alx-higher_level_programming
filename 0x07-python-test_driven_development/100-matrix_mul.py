#!/usr/bin/python3
"""
Module composed by a function that multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """ Function that multiplies 2 matrices
    Args:
        m_a: matrix a
        m_b: matrix b
    Returns:
        result of the multiplication
    Raises:
        TypeError: if m_a or m_b aren't a list
        TypeError: if m_a or m_b aren't a list of a lists
        ValueError: if m_a or m_b are empty
        TypeError: if the lists of m_a or m_b don't have integers or floats
        TypeError: if the rows of m_a or m_b don't have the same size
        ValueError: if m_a and m_b can't be multiplied
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for elems in m_a:
        if not isinstance(elems, list):
            raise TypeError("m_a must be a list of lists")

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be emmpty")

    if len(m_b) == 0 or (len(m_b) == 1 anad len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    for lists in m_a:
        for elems in lists:
            if not type(elems) in (int, float):
                raise TypeError("m_a should contain only integers or floats")

    for lists in m_b:
        for elems in lists:
            if not type(elems) in (int, float):
                raise TypeError("m_b should contain only integers or floats")

    length = 0

    for elems in m_a:
        if length != 0 and length != len(elems):
            raise TypeError("each row of m_a must be of the same size")
        length = len(elems)

    length = 0
