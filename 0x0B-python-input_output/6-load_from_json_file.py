#!/usr/bin/python3

""" Creates an Object from a JSON file """
import json


def load_from_json_file(filename):
    """
    Args:
        filename (file): The json file
    """
    with open(filename) as f:
        return json.load(f)
