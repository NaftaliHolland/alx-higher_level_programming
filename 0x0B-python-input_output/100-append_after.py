#!/usr/bin/python3
""" append_after """


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file after each line"""

    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    with open(filename, "w", encoding="utf-8") as f:
        new = ""
        for line in lines:
            new += line
            if search_string in line:
                new += new_string
        f.write(new)
