#!/usr/bin/python3

"""
Inserts a line of text to a file,
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Args:
        filename (file): The file to be altered
        search_string (str): The string to append new_string
        new_string (str): The string appended
    """

    text = ""
    with open(filename) as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as f:
        f.write(text)
