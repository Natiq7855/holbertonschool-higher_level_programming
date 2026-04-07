#!/usr/bin/python3
"""
This module defines the BaseGeometry class.
It serves as a foundation for all geometry-related objects in this project.
"""


class BaseGeometry:
    """
    BaseGeometry is the base class for geometric shapes.
    It provides methods for area calculation and input validation.
    """

    def area(self):
        """
        Calculates the area of the geometry shape.

        Raises:
            Exception: Because the area calculation is not implemented
            in this base class.
        """
        
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the provided value is a positive integer.

        Args:
            name (str): The name associated with the value being validated.
            value (int): The integer value to be checked.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """rectangle class"""

    def __init__(self, width, height):
        """set width and height"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
