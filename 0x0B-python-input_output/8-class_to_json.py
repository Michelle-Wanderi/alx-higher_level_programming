#!/usr/bin/python3

""" Returns the dictionary description for JSON serialization """


def class_to_json(obj):
    """
    Args:
        obj (any): The data structure
    """
    return obj.__dict__
