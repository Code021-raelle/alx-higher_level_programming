#!/usr/bin/python3

"""Module that defines a square"""


class Square:

    def __init__(self, size=0):
        """Initializing the square class
        Args:
            size: represents the size of the square defined
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
