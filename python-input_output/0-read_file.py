#!/usr/bin/python3
"""file for func"""


def read_file(filename=""):
    """read file func"""
    
    with open(filename, encoding="UTF-8") as file:
        print(file.read())
