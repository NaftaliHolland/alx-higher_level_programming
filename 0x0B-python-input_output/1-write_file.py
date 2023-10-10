#!/usr/bin/python3
"""Module documentation"""


def write_file(filename="", text=""):
    """Writes to a file

    Args:
        filename (string): name of the file
        text (string): text to be written to file

    Retruns: number of bytes writen
    """

    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(str(text))
