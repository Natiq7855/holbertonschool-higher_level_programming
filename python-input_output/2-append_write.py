#!/usr/bin/python3
"""append func"""


def append_write(filename="", text=""):
    """function of append"""

    with open(filename, mode="a", encoding="UTF-8") as f:
        f.write(text)
        return len(text)
