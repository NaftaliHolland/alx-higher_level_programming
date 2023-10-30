#!/usr/bin/python3
"""This file contains one function text_indentation"""


def text_indentation(text):
    """Prints a text with 2 new lines after (., ?, :)"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in text:
        if char in ('.', '?', ':'):
            print(f"{char}".strip())
            print()
        else:
            print(f"{char}", end="")
    print()
