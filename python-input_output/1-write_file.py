#!/usr/bin/python3
"""write func"""


def write_file(filename="", text=""):
    """write function"""

    with open(filename, mode="w", encoding="UTF_8") as file:
        file.write(text)
        return len(text)
