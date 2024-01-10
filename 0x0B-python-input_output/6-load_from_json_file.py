#!/usr/bin/python3
"""This module defines a JSON file-reading function"""
import json


def load_from_json_file(filename):
    """Creates a python object from a given JSON file"""
    with open(filename) as f:
        return json.load(f)
