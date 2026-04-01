#!/usr/bin/python3
"""
This module defines a Square class.
It is part of a series of exercises on Object-Oriented Programming.
"""


class Square:
    """An empty class Square that defines a square."""
    def __init__(self, size):
        """
        Initializes the square with a specific size.

        Args:
            size: The size of the square (no type/value verification).
        """
        self.__size = size
