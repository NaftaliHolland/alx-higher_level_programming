#!/usr/bin/python3
"""Module documentation"""


def read_file(filename=""):
    """reads a file and writes it to stdout"""

    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
