#!/usr/bin/python3
# base.py
""" Defines a base model class """
import json
import csv
import turtle


class Base:
    """Represent the base model
    Represents the "base" for all other classes in project 0x0C*.
    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor for the Base class

        Args:
            id (int, optional): Explicit id for the object. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
