#!/usr/bin/python3

""" Open and write into a file """


def write_file(filename="", text=""):
    """
    Args:
        filename (file): The file to write into.
        text (text): The text to write.
    Returns:
        Number of characters written.
    """
    with open(filename, 'w', encoding="UTF8") as f:
        char = f.write(text)

    return char

