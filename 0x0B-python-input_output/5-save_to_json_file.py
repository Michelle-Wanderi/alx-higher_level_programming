#!/usr/bin/python3

""" Writes an object file to a text file using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):

 """
    Args:
        my_obj (any): The Object to write to file
        filename (file): The json file
    """
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
