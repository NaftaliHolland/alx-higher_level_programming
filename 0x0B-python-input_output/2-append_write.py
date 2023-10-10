#!/usr/bin/python3
"""Module documentation"""


def append_write(filename="", text=""):
    """Appends a string to a file

    Args:
        filename (string): name of the file
        test (strint): string to be appended to file

    Returns: Number of characters added
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
