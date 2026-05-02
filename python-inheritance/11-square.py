#!/usr/bin/python3
"""
This module defines the Square class.
It inherits from the Rectangle class and implements specific square logic.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square, inheriting from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square's sides.

        Note:
            The size is validated as a positive integer using
            integer_validator and stored as a private attribute.
        """
        self.integer_validator("size", size)
        self.__size = size
        # Initialize the Rectangle parent with size for both width and height
        super().__init__(size, size)

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area (size squared).
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns the square description in a specific format.

        Format: [Square] <width>/<height>
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
