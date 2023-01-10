#!/usr/bin/python3

""" Append text to file """


def append_write(filename="", text=""):
    """
    Args:
        filename (file): The file to append text to.
        text: Characters to append to file.

    Returbs:
        Number of characters appended.
    """
    with open(filename, 'a', encoding="UTF8") as f:
        char = f.write(text)

    return char
