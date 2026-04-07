#!/usr/bin/python3
"""
This module defines the BaseGeometry class.
It serves as a foundation for all geometry-related objects in this project.
"""


class BaseGeometry():
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
        ads asdasd
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
