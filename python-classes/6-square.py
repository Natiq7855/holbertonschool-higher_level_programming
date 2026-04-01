#!/usr/bin/python3
"""
This module defines a Square class.
It is part of a series of exercises on Object-Oriented Programming.
"""


class Square:
    """An empty class Square that defines a square."""
    def __init__(self, size=0, position=(0,0)):
        """
        Initializes the square with a specific size.

        Args:
            size: The size of the square (no type/value verification).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            The private __size attribute.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates the current square area.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def position(self):
        """
        Retrieves the size of the square.

        Returns:
            The private __size attribute.
        """
        return self.__position

    def position(self, value):
        """
        Sets the size of the square with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
        """
        if self.__position[0] < 0 or self.__position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(self.__position, int):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """Prints the square with the # character."""
        if self.__size == 0:
            print("")
            return
        for i in range(self.__position[0]):
            print(" " * self.__position[0])
        for i in range(self.__size):
            print(" " * self.__position[1], end = '')
            print("#" * self.__size)
